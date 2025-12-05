from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import json
from chatbot_engine import AlumniChatbot

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

# Initialize chatbot
chatbot = None

@app.route('/')
def index():
    """Serve the chatbot interface"""
    return render_template('index.html')

@app.route('/api/initialize', methods=['POST'])
def initialize():
    """Initialize chatbot with CSV file"""
    global chatbot
    try:
        data = request.json
        csv_path = data.get('csv_path')
        
        if not os.path.exists(csv_path):
            return jsonify({'error': 'CSV file not found'}), 400
        
        chatbot = AlumniChatbot(csv_path)
        return jsonify({
            'status': 'success',
            'message': f'Chatbot initialized with {len(chatbot.data)} records'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    global chatbot
    try:
        if chatbot is None:
            return jsonify({'error': 'Chatbot not initialized. Please upload a CSV file first.'}), 400
        
        data = request.json
        user_message = data.get('message')
        
        if not user_message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        response = chatbot.process_query(user_message)
        return jsonify({
            'status': 'success',
            'response': response,
            'type': 'text'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/upload', methods=['POST'])
def upload():
    """Upload and process CSV file"""
    global chatbot
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not file.filename.endswith('.csv'):
            return jsonify({'error': 'Only CSV files are supported'}), 400
        
        # Save file
        upload_folder = 'uploads'
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        
        filepath = os.path.join(upload_folder, file.filename)
        file.save(filepath)
        
        # Initialize chatbot with the uploaded file
        chatbot = AlumniChatbot(filepath)
        
        return jsonify({
            'status': 'success',
            'message': f'CSV uploaded successfully. Found {len(chatbot.data)} alumni records.',
            'columns': chatbot.get_columns()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stats', methods=['GET'])
def stats():
    """Get statistics about the alumni database"""
    global chatbot
    try:
        if chatbot is None:
            return jsonify({'error': 'Chatbot not initialized'}), 400
        
        stats = chatbot.get_stats()
        return jsonify({'status': 'success', 'stats': stats})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/suggestions', methods=['GET'])
def suggestions():
    """Get suggested queries"""
    return jsonify({
        'status': 'success',
        'suggestions': [
            'How many alumni are there?',
            'Which year has the most alumni?',
            'What companies do alumni work in?',
            'What are the top skills among alumni?',
            'Show me alumni from [year]',
            'Find alumni working at [company]',
            'Which branch has the most alumni?'
        ]
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)

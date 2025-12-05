# Alumni Database Chatbot

A conversational chatbot for querying and analyzing alumni database CSV files. Supports natural language queries for alumni information including search, filtering, statistics, and analytics.

## Features

- **Upload CSV Files**: Upload your alumni database in CSV format
- **Natural Language Queries**: Ask questions about alumni in plain English
- **Smart Search**: Filter alumni by various criteria
- **Statistics**: Get distribution and analytics about your alumni
- **Responsive UI**: Works on desktop, tablet, and mobile devices
- **Real-time Processing**: Get instant responses to your queries

## Prerequisites

- Python 3.8+
- pip (Python package installer)

## Installation

1. Navigate to the chatbot directory:
```bash
cd chatbot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Chatbot

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

3. Upload your alumni CSV file using the "Upload CSV" button

4. Start asking questions about your alumni!

### Example Queries

- **Count Queries**: "How many alumni are there?"
- **Filter Queries**: "Show me alumni from 2020" or "Find alumni working at Google"
- **Statistics**: "What are the top companies?" or "Distribution of alumni by branch"
- **Information**: "What's in the database?"

## CSV Format

Your CSV file should have columns for alumni information. Common columns include:
- Name
- Year (graduation year)
- Company
- Branch
- Position
- Skills
- Location

The chatbot will automatically detect and work with any columns in your CSV.

## File Structure

```
chatbot/
├── app.py                 # Flask application
├── chatbot_engine.py      # Chatbot logic and query processing
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Frontend HTML
├── static/
│   ├── style.css         # Styling
│   └── script.js         # Frontend JavaScript
└── uploads/              # Uploaded CSV files (auto-created)
```

## API Endpoints

- `GET /` - Serves the chatbot interface
- `POST /api/chat` - Process chat messages
- `POST /api/upload` - Upload CSV file
- `GET /api/stats` - Get database statistics
- `GET /api/suggestions` - Get suggested queries
- `POST /api/initialize` - Initialize with CSV path

## Query Processing

The chatbot uses intelligent pattern matching to understand:
- **Count queries**: "how many", "count", "total", "number of"
- **Filter queries**: "where", "find", "show", "list", "from"
- **Statistics**: "stats", "distribution", "top", "most"
- **General info**: "what", "who", "information", "about"

## Customization

You can modify the chatbot behavior by editing:
- `chatbot_engine.py` - Query processing logic
- `static/style.css` - UI styling
- `templates/index.html` - HTML structure

## Troubleshooting

### Port Already in Use
If port 5000 is already in use, change it in `app.py`:
```python
app.run(debug=True, port=5001)
```

### CSV File Issues
- Ensure your CSV file is properly formatted
- Check that column names don't have special characters
- Ensure CSV encoding is UTF-8

### CORS Issues
The application has CORS enabled for development. For production, update the CORS configuration in `app.py`.

## Future Enhancements

- Advanced NLP with transformer models
- Database integration
- Export results to CSV/PDF
- User authentication
- Query history and saved searches
- Advanced analytics and visualizations

## License

MIT License

## Support

For issues or questions, please create an issue in the repository.

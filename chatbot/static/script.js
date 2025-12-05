// DOM Elements
const messageInput = document.getElementById('messageInput');
const sendBtn = document.getElementById('sendBtn');
const chatContainer = document.getElementById('chatContainer');
const fileInput = document.getElementById('fileInput');
const dbInfo = document.getElementById('dbInfo');
const sidebar = document.getElementById('sidebar');
const toggleMenu = document.getElementById('toggleMenu');
const toast = document.getElementById('toast');

let chatbotInitialized = false;
let isLoading = false;

// Event Listeners
sendBtn.addEventListener('click', sendMessage);
messageInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && !isLoading) {
        sendMessage();
    }
});

fileInput.addEventListener('change', handleFileUpload);
toggleMenu.addEventListener('click', toggleSidebar);

// Close sidebar when clicking outside on mobile
document.addEventListener('click', (e) => {
    if (window.innerWidth <= 768) {
        if (!sidebar.contains(e.target) && !toggleMenu.contains(e.target)) {
            sidebar.classList.remove('active');
        }
    }
});

function toggleSidebar() {
    sidebar.classList.toggle('active');
}

function sendMessage() {
    const message = messageInput.value.trim();
    
    if (!message) {
        showToast('Please type a message', 'error');
        return;
    }

    if (!chatbotInitialized) {
        showToast('Please upload a CSV file first', 'error');
        return;
    }

    if (isLoading) return;

    // Clear input
    messageInput.value = '';

    // Add user message to chat
    addMessageToChat(message, 'user');

    // Show loading state
    isLoading = true;
    sendBtn.disabled = true;
    messageInput.disabled = true;

    // Send to backend
    fetch('/api/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            showToast(data.error, 'error');
        } else {
            addMessageToChat(data.response, 'bot');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showToast('Failed to send message', 'error');
    })
    .finally(() => {
        isLoading = false;
        sendBtn.disabled = false;
        messageInput.disabled = false;
        messageInput.focus();
    });
}

function addMessageToChat(message, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}`;

    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    
    // Convert markdown-like formatting to HTML
    let htmlContent = message
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/\n/g, '<br>');
    
    contentDiv.innerHTML = htmlContent;
    messageDiv.appendChild(contentDiv);

    chatContainer.appendChild(messageDiv);

    // Scroll to bottom
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

function handleFileUpload() {
    const file = fileInput.files[0];

    if (!file) return;

    if (!file.name.endsWith('.csv')) {
        showToast('Please select a CSV file', 'error');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    showToast('Uploading CSV file...', 'info');

    fetch('/api/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            showToast(data.error, 'error');
        } else {
            chatbotInitialized = true;
            showToast(data.message, 'success');
            
            // Clear welcome message and show chat interface
            if (chatContainer.querySelector('.welcome-message')) {
                chatContainer.innerHTML = '';
                addMessageToChat(
                    `Great! I've loaded your alumni database with ${data.message.match(/\d+/)[0]} records. ` +
                    `I can now answer questions about your alumni. Try asking something like "How many alumni are there?" or "Show me alumni from 2020"`,
                    'bot'
                );
            }
            
            // Update database info
            updateDBInfo(data);
            
            // Reset file input
            fileInput.value = '';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showToast('Failed to upload file', 'error');
    });
}

function updateDBInfo(data) {
    if (!data.columns) return;

    dbInfo.innerHTML = `
        <div class="stat">
            <span>Total Records:</span>
            <span class="stat-value">${data.message.match(/\d+/)[0]}</span>
        </div>
        <div class="stat">
            <span>Columns:</span>
            <span class="stat-value">${data.columns.length}</span>
        </div>
        <p style="margin-top: 10px; font-size: 12px; color: var(--light-text);">
            <strong>Database Fields:</strong><br>
            ${data.columns.slice(0, 5).join(', ')}${data.columns.length > 5 ? '...' : ''}
        </p>
    `;
}

function suggestQuery(btn) {
    const query = btn.textContent;
    messageInput.value = query;
    messageInput.focus();
}

function showToast(message, type = 'info') {
    toast.textContent = message;
    toast.className = `toast show ${type}`;

    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

// Load suggestions on page load
function loadSuggestions() {
    fetch('/api/suggestions')
        .then(response => response.json())
        .then(data => {
            if (data.suggestions) {
                const suggestionsContainer = document.querySelector('.suggestions');
                suggestionsContainer.innerHTML = '';
                
                data.suggestions.forEach(suggestion => {
                    const btn = document.createElement('button');
                    btn.className = 'suggestion-btn';
                    btn.textContent = suggestion;
                    btn.onclick = () => suggestQuery(btn);
                    suggestionsContainer.appendChild(btn);
                });
            }
        })
        .catch(error => console.error('Error loading suggestions:', error));
}

// Initialize on load
window.addEventListener('load', () => {
    loadSuggestions();
    messageInput.focus();
});

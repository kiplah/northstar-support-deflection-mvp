from flask import Flask, render_template, request, jsonify, send_from_directory
import sqlite3
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    # Serves the basic chat interface
    return render_template('index.html')

@app.route('/chat')
def chat_page():
    # Serve chat.html from the frontend folder
    return send_from_directory(os.path.join(os.path.dirname(__file__), 'frontend'), 'chat.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    # This is where Ian's chat interface (Task 7) meets Meshack's logic (Tasks 8, 9, 10)
    data = request.json
    user_message = data.get("message", "")
    
    # Placeholder for intent routing
    # 1. Classify if order status, returns, or other
    # 2. Call the respective service (order_service or returns_service)
    # 3. Return the response
    
    return jsonify({
        "response": f"Echo: You said '{user_message}'. (Backend integration pending)", 
        "intent": "unknown"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)

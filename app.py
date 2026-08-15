from flask import Flask, render_template, request, jsonify, send_from_directory
import os

# pyright: reportMissingImports=false
from services.intent_router import route_intent

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/chat')
def chat_page():
    # Serve chat.html from the frontend folder
    return send_from_directory(os.path.join(os.path.dirname(__file__), 'frontend'), 'chat.html')


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    user_message = data.get("message", "")

    result = route_intent(user_message)

    return jsonify({
        "response": result.get("response", ""),
        "intent": result.get("intent", "")
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)
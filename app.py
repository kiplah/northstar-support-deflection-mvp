# pyright: reportMissingImports=false
from flask import Flask, render_template, request, jsonify  # type: ignore
from services.intent_router import route_intent

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    result = route_intent(user_message)

    return jsonify({
        "response": result["response"],
        "intent": result["intent"]
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)
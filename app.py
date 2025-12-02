from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    msg = data.get("message", "")

    payload = {
        "model": "phi",
        "prompt": msg,
        "stream": False
    }

    res = requests.post(OLLAMA_URL, json=payload).json()
    return jsonify({"response": res.get("response", "")})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

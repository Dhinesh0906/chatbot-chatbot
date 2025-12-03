import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

OLLAMA_URL = os.environ.get("OLLAMA_URL")
if not OLLAMA_URL:
    raise ValueError("Environment variable OLLAMA_URL is not set.")

@app.route("/")
def home():
    return {"status": "API running", "ollama_url": OLLAMA_URL}

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "")

        payload = {
            "model": "phi",
            "prompt": prompt
        }

        res = requests.post(f"{OLLAMA_URL}/api/generate", json=payload)
        res.raise_for_status()

        return jsonify(res.json())

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

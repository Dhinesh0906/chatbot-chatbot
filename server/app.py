from flask import Flask, request, jsonify
from llama_cpp import Llama

app = Flask(__name__)

llm = Llama(
    model_path="model/tinyllama.gguf",
    n_ctx=2048,
    n_threads=4,
    temperature=0.2,
    top_p=0.9,
    repeat_penalty=1.1
)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("prompt", "")

    output = llm(prompt, max_tokens=200)
    text = output["choices"][0]["text"].strip()

    return jsonify({"response": text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

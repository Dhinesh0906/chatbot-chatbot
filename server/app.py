from fastapi import FastAPI
from pydantic import BaseModel
from llama_cpp import Llama
import os

app = FastAPI()

model_path="model/tinyllama.gguf"


# Load the model
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,
    n_threads=4,
    temperature=0.2,
    top_p=0.9,
    repeat_penalty=1.1,
    verbose=False
)

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
def chat(req: ChatRequest):
    output = llm(req.prompt, max_tokens=200)
    text = output["choices"][0]["text"].strip()
    return { "response": text }


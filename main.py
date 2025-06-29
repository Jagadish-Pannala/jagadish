import os
os.environ["LANGCHAIN_API_KEY"] = "off"
os.environ["LANGCHAIN_TRACING_V2"] = "false"
os.environ["LANGCHAIN_ENDPOINT"] = ""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from app.chatbot import chat_with_bot

app = FastAPI()

class Query(BaseModel):
    message: str

@app.post("/chat")
def chat(query: Query):
    try:
        exit_keywords = ['exit', 'quit', 'bye']
        if query.message.strip().lower() in exit_keywords:
            return {"response": "Goodbye! Chat ended.", "end": True}

        answer = chat_with_bot(query.message)
        return {"response": answer, "end": False}
    except Exception as e:
        return {"error": str(e), "end": True}


# ✅ Serve frontend
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def serve_index():
    return FileResponse("frontend/index.html")

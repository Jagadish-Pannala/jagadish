from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from app.chatbot import chat_with_bot
from fastapi.staticfiles import StaticFiles

app = FastAPI()

class Query(BaseModel):
    message: str

@app.post("/chat")
def chat(query: Query):
    try:
        answer = chat_with_bot(query.message)
        return {"response": answer}
    except Exception as e:
        return {"error": str(e)}

# ✅ Serve frontend

app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def serve_index():
    return FileResponse("frontend/index.html")

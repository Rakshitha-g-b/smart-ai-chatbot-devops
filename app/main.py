import os
import time
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response
from openai import OpenAI

app = FastAPI(title="Smart AI Chatbot DevOps Project")
templates = Jinja2Templates(directory="app/templates")

REQUEST_COUNT = Counter("chatbot_requests_total", "Total HTTP requests")
CHAT_REQUESTS = Counter("chatbot_chat_requests_total", "Total chatbot requests")
REQUEST_LATENCY = Histogram("chatbot_request_latency_seconds", "Request latency in seconds")

api_key = os.getenv("OPENROUTER_API_KEY")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
) if api_key else None

conversation_histories = {}

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    REQUEST_COUNT.inc()
    response = await call_next(request)
    REQUEST_LATENCY.observe(time.time() - start_time)
    return response

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat(message: str = Form(...), session_id: str = Form("default")):
    CHAT_REQUESTS.inc()

    if client is None:
        return JSONResponse({"reply": "API key missing. Set OPENROUTER_API_KEY first."})

    if session_id not in conversation_histories:
        conversation_histories[session_id] = [
            {
                "role": "system",
                "content": "You are a helpful AI chatbot. Answer like ChatGPT or Perplexity: natural, clear, and concise."
            }
        ]

    conversation_histories[session_id].append({"role": "user", "content": message})

    try:
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=conversation_histories[session_id]
        )
        reply = response.choices[0].message.content
        conversation_histories[session_id].append({"role": "assistant", "content": reply})
        return JSONResponse({"reply": reply})
    except Exception as e:
        return JSONResponse({"reply": f"Error contacting model: {str(e)}"})

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/metrics")
async def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
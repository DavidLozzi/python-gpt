import openai
import logging
import json
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.encoders import jsonable_encoder
from app.RequestQuery import RequestQuery
from app.stream import stream

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")

app = FastAPI()

logging.basicConfig(format="%(levelname)s:     %(message)s", level=logging.INFO)
log = logging.getLogger(__name__)


@app.post("/chat")
async def chat(request: RequestQuery):
    messages = jsonable_encoder(request.messages)

    log.info(f"Calling openai with {messages}")
    response = openai.ChatCompletion.create(
        model=request.engine,
        messages=messages,
    )
    return response


@app.post("/stream")
def chat(request: RequestQuery):
    return StreamingResponse(stream(request), media_type="text/event-stream")

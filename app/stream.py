import logging
import json
import openai
from fastapi.encoders import jsonable_encoder
from app.RequestQuery import RequestQuery

log = logging.getLogger(__name__)


def stream(request: RequestQuery):
    messages = jsonable_encoder(request.messages)
    log.info(f"Calling openai with {messages}")
    response = openai.ChatCompletion.create(
        model=request.engine,
        messages=messages,
        stream=True,
    )

    for chunk in response:
        print(chunk)
        chunk.pop("id", None)
        chunk.pop("object", None)
        chunk.pop("created", None)
        chunk.pop("model", None)
        yield f"data: {json.dumps(chunk)}\n\n"

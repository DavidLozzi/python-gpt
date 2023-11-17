from pydantic import BaseModel
from app.Message import Message
from typing import List


class RequestQuery(BaseModel):
    messages: List[Message]
    engine: str = "gpt-3.5-turbo"
    temperature: float = 0.9
    max_tokens: int = 2000

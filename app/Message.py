import json
from pydantic import BaseModel


class Message(BaseModel):
    role: str
    content: str

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

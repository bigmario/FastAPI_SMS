from pydantic import BaseModel

class Sms(BaseModel):
    to : str
    body : str
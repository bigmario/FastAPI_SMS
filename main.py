
from fastapi import FastAPI, Form, status
from fastapi.responses import JSONResponse

from sms.controller import sms_router

from utils.remove_422 import remove_422



app = FastAPI()

app.include_router(sms_router)

@app.get('/')
@remove_422
async def index():
    return JSONResponse({'message': 'FastAPI Send SMS via Twilio!!'})





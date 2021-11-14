from fastapi import FastAPI
from fastapi.responses import JSONResponse

from sms.controller import sms_router

from utils.remove_422 import remove_422


app = FastAPI()

app.include_router(sms_router)


@app.get(path="/", summary="Index", tags=["Index"])
@remove_422
async def index():
    return JSONResponse({"Hello": "FastAPI Send SMS via Twilio!!"})

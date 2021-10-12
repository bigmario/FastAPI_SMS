from __future__ import annotations
from fastapi import APIRouter, status, Form, status

from error_handlers.schemas.bad_gateway import BadGatewayError
from error_handlers.schemas.unauthorized import UnauthorizedError

from .schemas.post_sms import Sms

from utils.remove_422 import remove_422

from .service.sms_service import SmsService


sms_router = APIRouter(
    tags=["SMS"],
    responses={
        status.HTTP_502_BAD_GATEWAY: {"model": BadGatewayError},
        status.HTTP_401_UNAUTHORIZED: {"model": UnauthorizedError},
    },
)

@sms_router.post("/sms",
                response_model_exclude_unset=True,
                responses={status.HTTP_401_UNAUTHORIZED: {"model": UnauthorizedError}})
@remove_422
async def send_sms(body : Sms):
    """
    Send SMS from Body:
    """
    sms_service: SmsService = SmsService()
    return await sms_service.handle_form(body)
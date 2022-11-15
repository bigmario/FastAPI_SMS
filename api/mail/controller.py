from fastapi import Body, BackgroundTasks
from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse

from api.error_handlers.schemas.bad_gateway import BadGatewayError
from api.error_handlers.schemas.unauthorized import UnauthorizedError
from api.error_handlers.schemas.not_found import NotFoundError

from .schemas.post_email import Email

from api.utils.remove_422 import remove_422

from .service.email_service import EmailService


email_router = APIRouter(
    tags=["EMAIL"],
    responses={
        status.HTTP_502_BAD_GATEWAY: {"model": BadGatewayError},
        status.HTTP_401_UNAUTHORIZED: {"model": UnauthorizedError},
        status.HTTP_404_NOT_FOUND: {"model": NotFoundError},
    },
)


@email_router.post(
    path="/email",
    status_code=status.HTTP_200_OK,
    summary="Send EMAIL",
    response_model_exclude_unset=True,
)
@remove_422
async def send_email(
    body: Email = Body(...),
    email_service: EmailService = Depends(),
):
    """
    Send Email from Body:
    """
    return await email_service.send_email(body)


@email_router.post("/send-email/asynchronous")
async def send_email_asynchronous(
    body: Email = Body(...),
    email_service: EmailService = Depends(),
):
    await email_service.send_email_async(body)
    return JSONResponse(
        {"Message": "Email Successfully Sent!!"}, status_code=status.HTTP_200_OK
    )


@email_router.post("/send-email/backgroundtasks")
def send_email_backgroundtasks(
    background_tasks: BackgroundTasks,
    body: Email = Body(...),
    email_service: EmailService = Depends(),
):
    email_service.send_email_background(background_tasks, body)
    return JSONResponse(
        {"Message": "Email Successfully Sent!!"}, status_code=status.HTTP_200_OK
    )

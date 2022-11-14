from typing import List
from beanie import PydanticObjectId
from fastapi import APIRouter, BackgroundTasks, Body, status, Path

from api.error_handlers.schemas.bad_gateway import BadGatewayError
from api.error_handlers.schemas.not_found import NotFoundError
from api.error_handlers.schemas.unauthorized import UnauthorizedError
from api.utils.remove_422 import remove_422

from .schemas.subscriptions import Subscription
from .service.subscription_service import SubscriptionService


########################
# Subscription Router
########################

subscription_router = APIRouter(
    tags=["Subscription"],
    responses={
        status.HTTP_502_BAD_GATEWAY: {"model": BadGatewayError},
        status.HTTP_401_UNAUTHORIZED: {"model": UnauthorizedError},
        status.HTTP_404_NOT_FOUND: {"model": NotFoundError},
    },
)

########################
# Create a subscription
########################


@subscription_router.post(
    path="/subscription",
    status_code=status.HTTP_200_OK,
    summary="Subscribe",
    response_model_exclude_unset=True,
)
@remove_422
async def subscribe(body: Subscription = Body(...)):
    """
    Subscribe:
    """
    subscription_service: SubscriptionService = SubscriptionService()
    return await subscription_service.subscribe(body)


########################
# GET ALL SUBSCRIPTIONS
########################


@subscription_router.get(
    path="/subscription",
    status_code=status.HTTP_200_OK,
    summary="Get All Subscriptions",
    response_model_exclude_unset=True,
)
@remove_422
async def get_one_subscription() -> List[Subscription]:
    subscription_service: SubscriptionService = SubscriptionService()
    return await subscription_service.get_all_subscriptions()


#############################
# GET ONE SUBSCRIPTION BY ID
#############################


@subscription_router.get(
    path="/subscription/{id}",
    status_code=status.HTTP_200_OK,
    summary="Get One Subscription By ID",
    response_model_exclude_unset=True,
)
@remove_422
async def get_one_subscription(id: PydanticObjectId = Path(...)) -> Subscription:
    subscription_service: SubscriptionService = SubscriptionService()
    return await subscription_service.get_one_subscription(id)


@subscription_router.delete(
    path="/subscription/{id}",
    status_code=status.HTTP_200_OK,
    summary="Delete One Subscription By ID",
    response_model_exclude_unset=True,
)
@remove_422
async def delete_student_data(id: PydanticObjectId = Path(...)) -> dict:
    subscription_service: SubscriptionService = SubscriptionService()
    return await subscription_service.delete_subscription(id)

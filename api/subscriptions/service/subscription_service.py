import os
from typing import List
from beanie import PydanticObjectId
from fastapi import Body, HTTPException, status
from fastapi.responses import JSONResponse

from api.error_handlers.schemas.not_found import NotFoundError

from api.subscriptions.schemas.subscriptions import Subscription


class SubscriptionService:
    async def subscribe(self, body: Subscription = Body(...)):
        existing_sub = await Subscription.find_one(Subscription.mail == body.mail)

        if not existing_sub:
            await body.create()
            return JSONResponse(
                {"Message": "Subscribed!!"}, status_code=status.HTTP_200_OK
            )
        else:
            return JSONResponse(
                {"Message": "Existing Email!!"}, status_code=status.HTTP_400_BAD_REQUEST
            )

    async def get_all_subscriptions(self) -> List[Subscription]:
        return await Subscription.find_all().to_list()

    async def get_one_subscription(self, id: PydanticObjectId) -> Subscription:
        return await Subscription.get(id)

    async def delete_subscription(self, id: PydanticObjectId) -> dict:
        sub = await Subscription.get(id)

        if not sub:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Subscription not found!"
            )

        await sub.delete()
        return {"message": "Subscription deleted successfully"}

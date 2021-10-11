
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from sms.config import config

from sms.schemas.post_sms import Sms

import asyncio


settings = config.Settings()

class SmsService():

    def send_sms(self, body: Sms):
        failure = {"code": 400, "message": "Can't send SMS"}
        client = Client(settings.twilio_account_sid, settings.twilio_auth_token)
        client.messages.create(from_ = settings.twilio_phone_number, to = body.to, body = body.body)

    async def handle_form(self, body: Sms):
        success = {"code": 200, "message": "SMS Sent Successfully"}
        asyncio.get_event_loop().run_in_executor(None, self.send_sms, body)
        return success
        
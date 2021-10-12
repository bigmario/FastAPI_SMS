
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from sms.config import config

import logging

from sms.schemas.post_sms import Sms

from fastapi.responses import JSONResponse


settings = config.Settings()

class SmsService():

    def send_sms(self, body: Sms):
        try:
            success = {"code": 200, "message": "SMS Sent Successfully"}
            client = Client(settings.twilio_account_sid, settings.twilio_auth_token)
            logging.basicConfig()
            client.http_client.logger.setLevel(logging.INFO)
            client.messages.create(from_ = settings.twilio_phone_number, to = body.to, body = body.body)
            return JSONResponse(success)
        except TwilioRestException as e:
            failure = {"code": 400, "message": f"Can't send SMS - {e}"}
            return JSONResponse(failure)
        
        
        
import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    twilio_account_sid: str = os.getenv('TWILIO_ACCOUNT_SID', 'AC7f4dd7efc19ecf258e69ac077f0650ca')
    twilio_auth_token: str = os.getenv('TWILIO_AUTH_TOKEN', '66c95ae9d816d201d0c563925cc7bb2e')
    twilio_phone_number: str = os.getenv('TWILIO_PHONE_NUMBER', '+12184133682')
import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    secret_key: str
    redis_url: str
    host: str
    log_level: str

    class Config:
        env_file = ".env"

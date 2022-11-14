import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    db_name: str
    secret_key: str
    redis_url: str
    host: str
    log_level: str
    reload: int

    class Config:
        env_file = ".env"

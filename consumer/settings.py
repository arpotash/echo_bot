import os

import pydantic


class Settings(pydantic.BaseSettings):
    broker_host: str = os.getenv("BROKER_HOST")
    broker_port: str = int(os.getenv("BROKER_PORT", "5672"))
    telegram_url: str = os.getenv("TELEGRAM_URL")
    telegram_char_id: int = int(os.getenv("TELEGRAM_CHAT_ID", "0"))


settings = Settings()

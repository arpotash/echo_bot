import os
import pydantic


class Settings(pydantic.BaseSettings):
    broker_host: str = os.getenv("BROKER_HOST")
    broker_port: int = int(os.getenv("BROKER_PORT", "5672"))
    producer_exchange: str = os.getenv("PRODUCER_EXCHANGE")
    producer_queue: str = os.getenv("PRODUCER_QUEUE")


settings = Settings()

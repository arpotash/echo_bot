import fastapi

from bot.resources.pika import PikaClient
from bot.api.tg import PRODUCER_ROUTER

app = fastapi.FastAPI()
app.include_router(PRODUCER_ROUTER)


@app.on_event("startup")
async def startup_event() -> None:
    pika_client = PikaClient()
    app.state.pika = pika_client


@app.on_event("shutdown")
async def shutdown_event() -> None:
    app.state.pika.close()

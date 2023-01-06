from fastapi import FastAPI
from consumer.resources.pika import PikaClient


app = FastAPI()


@app.on_event("startup")
def startup_event():
    pika_client = PikaClient()
    app.state.pika = pika_client
    pika_client.consume()


@app.on_event("shutdown")
async def shutdown_event() -> None:
    app.state.pika.close()

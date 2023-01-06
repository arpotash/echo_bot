import fastapi

from bot.schemas.bot import SendMessageSchema
from bot.services.message import Message

PRODUCER_ROUTER = fastapi.APIRouter(prefix="/api-v1", tags=["producer"])


@PRODUCER_ROUTER.post("/send")
def send_message(message_send_schema: SendMessageSchema, request: fastapi.Request):
    message_instance = Message(message_send_schema.message)
    compressed_message = message_instance.compress()
    request.app.state.pika.produce(compressed_message)

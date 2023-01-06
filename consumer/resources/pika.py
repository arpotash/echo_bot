import pika

from consumer.services.message import Message
from consumer.settings import settings
from consumer.services.message_translate import Telegram


class PikaClient:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=settings.broker_host)
        )
        self.channel = self.connection.channel()
        self.channel.exchange_declare("bot", durable=True, exchange_type="topic")
        self.channel.queue_declare(queue="tg")
        self.channel.queue_bind(exchange="bot", queue="tg", routing_key="tg")

    @staticmethod
    def callback_function(ch, method, properties, body):
        message_instance = Message(body)
        decompressed_message = message_instance.decompress()
        platform_instance = Telegram()
        platform_instance.send(decompressed_message)

    def consume(self):
        self.channel.basic_consume(queue="tg", on_message_callback=self.callback_function, auto_ack=True)
        self.channel.start_consuming()

    def close(self):
        self.channel.close()

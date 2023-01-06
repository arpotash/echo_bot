import pika
from bot.settings import settings


class PikaClient:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=settings.broker_host)
        )
        self.channel = self.connection.channel()
        self.channel.exchange_declare(settings.producer_exchange, durable=True, exchange_type="topic")
        self.channel.queue_declare(queue=settings.producer_queue)
        self.channel.queue_bind(
            exchange=settings.producer_exchange,
            queue=settings.producer_queue,
            routing_key=settings.producer_queue
        )

    def produce(self, message: bytes):
        self.channel.basic_publish(
            exchange=settings.producer_exchange,
            routing_key=settings.producer_queue, body=message
        )

    def close(self):
        self.channel.close()

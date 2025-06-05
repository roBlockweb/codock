import pika
from .config import Config

class QueueManager:
    def __init__(self):
        try:
            params = pika.ConnectionParameters(host=Config.RABBIT_HOST, port=Config.RABBIT_PORT)
            self.connection = pika.BlockingConnection(params)
            self.channel = self.connection.channel()
            self.channel.queue_declare(queue=Config.QUEUE_NAME)
        except Exception:
            self.connection = None
            self.channel = None

    def publish(self, message):
        if self.channel:
            self.channel.basic_publish(exchange='', routing_key=Config.QUEUE_NAME, body=message)

    def consume(self, callback):
        if self.channel:
            self.channel.basic_consume(queue=Config.QUEUE_NAME, on_message_callback=callback, auto_ack=True)
            self.channel.start_consuming()

from confluent_kafka import Consumer
from core.mediator import Mediator


class ConsumerService:
    mediator = Mediator

    def __init__(self, config: dict):
        self.consumer = Consumer(config)

    def add_subscribe(self, topic):
        self.consumer.subscribe([topic])
        self.consumer.list_topics()

    async def listen(self):
        try:
            msg = self.consumer.poll(1)
            while True:
                if msg is None:
                    print("Waiting")
                elif msg.error():
                    print(f"Consumer error: {msg.error()}")
                else:
                    self.mediator.notify(msg.value().decode("utf-8"))

                    print(
                        f"Produced event to topic {msg.topic()}: key = {msg.key()}, value = {msg.value().decode('utf-8')}"
                    )
        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            pass
        finally:
            self.consumer.close()

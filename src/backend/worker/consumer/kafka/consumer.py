from json import loads

from confluent_kafka import Consumer
from core.mediator import Mediator
from core.mediator.mediator import MediatorCommand


class ConsumerService:
    mediator = Mediator()

    def __init__(self, config: dict):
        self.consumer = Consumer(config)

    def add_subscribe(self, topic):
        self.consumer.subscribe(topic)

    async def listen(self):
        try:
            while True:
                msg = self.consumer.poll(1)
                print(msg)
                if msg is None:
                    pass
                elif msg.error():
                    print(f"Consumer error: {msg.error()}")
                else:
                    command = MediatorCommand(
                        command=msg.key().decode("utf-8"),
                        payload=loads(msg.value().decode("utf-8")),
                    )

                    await self.mediator.notify(command)

        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            pass
        finally:
            self.consumer.close()

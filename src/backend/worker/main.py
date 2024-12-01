from asyncio import run

from consumer.kafka import ConsumerService
from core.settings import KAFKA_LINK


async def main():
    kafka_consumer = ConsumerService(
        {
            "bootstrap.servers": KAFKA_LINK,
            "group.id": "all",
            "auto.offset.reset": "earliest",
        }
    )
    print("kafka configured")

    kafka_consumer.add_subscribe(["user", "report"])

    print("kafka subscription added")

    print("kafka start listening")
    await kafka_consumer.listen()


if __name__ == "__main__":
    run(main())

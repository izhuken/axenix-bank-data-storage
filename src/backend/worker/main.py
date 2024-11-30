from asyncio import run

from consumer.kafka import ConsumerService


async def main():
    kafka_consumer = ConsumerService(
        {
            "bootstrap.servers": "localhost:9092",
            "group.id": "all",
            "auto.offset.reset": "earliest",
        }
    )
    print("kafka configured")

    kafka_consumer.add_subscribe("tests")

    print("kafka subscription added")

    print("kafka start listening")
    await kafka_consumer.listen()


if __name__ == "__main__":
    run(main())

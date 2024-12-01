from asyncio import run

from .kafka import ConsumerService


async def main():
    kafka_consumer = ConsumerService({})
    kafka_consumer.add_subscribe([])


if __name__ == "__main__":
    run(main())

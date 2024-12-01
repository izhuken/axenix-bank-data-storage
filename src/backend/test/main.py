from json import dumps

from fastapi import FastAPI

app = FastAPI(url_docs="/docs/1")


from confluent_kafka import Producer

config = {"bootstrap.servers": "localhost:9092", "acks": "all", "group.id": "all"}

producer = Producer(config)


def delivery_callback(err, msg):
    if err:
        print(f"Error: Message failed delivery: {err}")
    else:
        print(
            f"Produced event to topic {msg.topic()}: key = {msg.key()}, value = {msg.value().decode('utf-8')}"
        )


topic = "tests"


@app.post("/")
async def aue():
    producer.produce(
        topic,
        dumps({"report": "test-report.csv", "user_id": "asdf-asdf-asdf-asdf"}),
        "create_transaction_task",
        callback=delivery_callback,
    )

    producer.produce(
        topic,
        dumps(
            {
                "customer_agreement": "str",
                "credit_products": "str",
                "credit_transactions": "str",
                "customers": "str",
                "transaction_types": "str",
            }
        ),
        "init_task",
        callback=delivery_callback,
    )

    producer.produce(
        topic,
        dumps(
            {
                "customer_type_id": 1,
                "name": "Тестовый Тест Тестович",
                "date_of_birth": "1994-01-12",
                "registration_date": "2024-01-12",
                "tin": "122333213",
                "contact_info": "+7 (912) 234-12-23",
            }
        ),
        "create_customer_task",
        callback=delivery_callback,
    )

    producer.poll(1)
    producer.flush()

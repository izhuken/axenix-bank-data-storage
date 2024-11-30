from os import getenv as env

from confluent_kafka import Producer
from dotenv import load_dotenv

load_dotenv()
config = {
    "bootstrap.servers": env("KAFKA_URL"),
    "acks": "all",
}
TOPIC_CREATE_USER = "user"
TOPIC_ACCEPT_REPORT = "report"

producer = Producer(config)
import json

from app.service.kafka_producer import KafkaService
from core.kafka_config import TOPIC_DATABASE_UPLOAD
from fastapi import APIRouter

# from service.upload_database i

upload_database_router = APIRouter(tags=["UploadCDatabase"])

kafka_service = KafkaService()


@upload_database_router.post("/upload_database", status_code=201)
async def upload_database() -> None:
    kafka_service.produce(key="init_task", value = json.dumps(
            {
                "customer_agreement": "str",
                "credit_products": "str",
                "credit_transactions": "str",
                "customers": "str",
                "transaction_types": "str",
            }
        ), topic = TOPIC_DATABASE_UPLOAD)
    return None
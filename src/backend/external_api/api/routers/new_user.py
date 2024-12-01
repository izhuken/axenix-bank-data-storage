import json

from app.schemas.new_user_schemas import CreateCustomerRequest
from app.service.kafka_producer import KafkaService
from app.service.s3 import BaseFileService
from core.kafka_config import TOPIC_CREATE_USER
from fastapi import APIRouter

new_user_router = APIRouter(tags=["NewUser"])

s3_service = BaseFileService()
kafka_service = KafkaService()


@new_user_router.post("/new_user", status_code=202)
async def new_user(data: CreateCustomerRequest) -> None:
    kafka_service.produce(key="report", 
                        value=json.dumps({"command": "create_customer_task", 
                                        "payload": {"customer_type_id": data["customer_type_id"],
                                                    "name": data["name"],
                                                    "date_of_birth": data["date_of_birth"],
                                                    "registration_date": data["registration_date"],
                                                    "tin": data["tin"],
                                                    "contact_info": data["contact_info"],
                                                    }}), topic=TOPIC_CREATE_USER)
    return None
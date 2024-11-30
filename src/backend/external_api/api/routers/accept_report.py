import json

import jwt
from app.service.kafka_producer import KafkaService
from app.service.s3 import BaseFileService
from core.config import ALGORITHM, SECRET_KEY
from core.kafka_config import TOPIC_ACCEPT_REPORT
from fastapi import APIRouter, File, Request, UploadFile

accept_report_router = APIRouter(tags=["AcceptReport"])

s3_service = BaseFileService()
kafka_service = KafkaService()


@accept_report_router.post("/accept_report", status_code=202)
async def accept_report(request: Request, file: UploadFile = File(...)) -> None:
    path_file = await s3_service.upload_file_to_s3(file, request)
    print(request.headers)
    jwt_token = request.headers["Authtorization"]
    user_id = jwt.decode(jwt_token, algorithms=ALGORITHM, key=SECRET_KEY)["user_id"]

    kafka_service.produce(key="report", value=json.dumps({"command": "create_transaction_task", "payload": {"user_id": user_id, "link_file": path_file}}), topic = TOPIC_ACCEPT_REPORT)
    return None
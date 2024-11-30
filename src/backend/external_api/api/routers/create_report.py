
from app.schemas.create_report_schemas import (
    CreateReportInsert,
    CreateReportRequest,
    CreateReportResponse,
)
from app.schemas.response import ErrorResponse
from app.service.builder_report import BuilderReportService
from app.service.external_report import ExternalReportService
from fastapi import APIRouter, HTTPException, Request

create_report_router = APIRouter(tags=["CreateReport"])
external_report_service = ExternalReportService()
# builder_report_service = BuilderReportService()

@create_report_router.post("/create_report", status_code=201, response_model=CreateReportResponse)
async def create_report(data: CreateReportRequest, request: Request) -> CreateReportResponse:
    # jwt_token = request.header('Authtorization')
    # user_id = jwt.decode(jwt_token, algorithms=ALGORITHM, key=SECRET_KEY)["user_id"]
    data_dict = data.model_dump()
    builder_report_service = BuilderReportService(data_dict["report_name"], data_dict["values"], data_dict["format_report"], request)
    path_file = await builder_report_service.create_file()
    print(path_file)
    result = await external_report_service.create(data=CreateReportInsert(**{"title": data.report_name, "url": path_file, "user_id": "30a18ed5-12f0-491e-993e-e55ae0997883"}))
    if isinstance(result, ErrorResponse):
        raise HTTPException(status_code=result.status_code, detail=result.detail)
    return result["url"]

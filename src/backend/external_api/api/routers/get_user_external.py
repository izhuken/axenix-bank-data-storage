from app.schemas.response import ErrorResponse
from app.service.external_report import ExternalReportService
from fastapi import APIRouter, HTTPException, Request

user_external_report_router = APIRouter(tags=["UserExternalReport"])
external_report_service = ExternalReportService()


@user_external_report_router.get("/get_user_external_report/{id}", status_code=200)
async def get_user_external_report(id,
                                request: Request,
                                page: int = 1,
                                quantity: int = 50,
                                order_by: str | None = None,
                                ):
    data = await external_report_service.get_all(request, page, quantity, order_by, user_id = id)
    if isinstance(data, ErrorResponse):
        raise HTTPException(status_code=data.status_code, detail=data.detail)

    return data
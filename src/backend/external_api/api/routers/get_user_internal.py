from app.schemas.response import ErrorResponse
from app.service.internal_report import InternalReportService
from fastapi import APIRouter, HTTPException, Request

user_internal_report_router = APIRouter(tags=["UserInternalReport"])
internal_report_service = InternalReportService()


@user_internal_report_router.get("/get_user_internal_report/{id}", status_code=200)
async def get_user_internal_report(id,
                                request: Request,
                                page: int = 1,
                                quantity: int = 50,
                                order_by: str | None = None,
                                ):
    data = await internal_report_service.get_all(request, page, quantity, order_by, user_id = id)
    if isinstance(data, ErrorResponse):
        raise HTTPException(status_code=data.status_code, detail=data.detail)

    return data
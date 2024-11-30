from repository.internal_report import InternalReportRepository

from app.schemas.get_user_internal_reports_schemas import UserInternalResponse

from ._base_service import BaseService


class InternalReportService(BaseService):
    _repository = InternalReportRepository()
    _serializer = UserInternalResponse

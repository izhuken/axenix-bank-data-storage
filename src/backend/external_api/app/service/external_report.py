from repository.external_report import ExternalReportRepository

from app.schemas.get_user_external_reports_schemas import UserExternalResponse

from ._base_service import BaseService


class ExternalReportService(BaseService):
    _repository = ExternalReportRepository()
    _serializer = UserExternalResponse

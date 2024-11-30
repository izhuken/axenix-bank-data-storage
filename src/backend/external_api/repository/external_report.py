from core.models.external_report import ExternalReport

from ._base_sqlalchemy_repository import BaseSQLAlchemyRepository


class ExternalReportRepository(BaseSQLAlchemyRepository):
    model = ExternalReport

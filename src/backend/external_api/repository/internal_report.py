from core.models.internal_report import InternalReport

from ._base_sqlalchemy_repository import BaseSQLAlchemyRepository


class InternalReportRepository(BaseSQLAlchemyRepository):
    model = InternalReport

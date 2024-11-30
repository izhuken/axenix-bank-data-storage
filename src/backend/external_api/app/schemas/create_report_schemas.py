from datetime import date
from enum import Enum
from uuid import UUID

from ._base import BaseSchema


class FileEnum(Enum):
    xls = "xlsx"
    csv = "csv"

class Value(BaseSchema):
    value: int
    field_name: str
    data_from: date
    date_to: date

class CreateReportRequest(BaseSchema):
    report_name: str
    values: list[Value]
    format_report: FileEnum

class CreateReportInsert(BaseSchema):
    title: str
    url: str
    user_id: UUID

class CreateReportResponse(BaseSchema):
    url: str

from uuid import UUID

from ._base import BaseSchema

# class AcceptReportRequest(BaseModel):
#     jwt: str
#     csv_or_excel_file: File

class AcceptReportResponse(BaseSchema):
    link_file: str
    user_id: UUID
from uuid import UUID

from pydantic import BaseModel


class UserExternalRequest(BaseModel):
    user_id: UUID

class UserExternalResponse(BaseModel):
    link_reports: list[str]

from uuid import UUID

from ._base import BaseSchema


class UserInternalRequest(BaseSchema):
    user_id: UUID

class UserInternalResponse(BaseSchema):
    link_reports: list[str]
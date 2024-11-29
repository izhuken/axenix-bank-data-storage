from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field

from ._base import BaseSchema


class UserBase(BaseSchema):
    username: str
    email: EmailStr
    phone: str
    rating: int
    is_admin: bool = Field(default=False)


class UserRead(UserBase):
    id: UUID
    is_active: bool
    create_time: datetime
    update_time: datetime


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    username: str | None = Field(default=None)
    email: EmailStr | None = Field(default=None)
    phone: str | None = Field(default=None)
    address: str | None = Field(default=None)
    is_admin: bool | None = Field(default=None)


# class UserSearch(BaseModel):
#     username: str | None = Field(default=None)
#     email: EmailStr | None = Field(default=None)
#     phone: str | None = Field(default=None)
#     address: str | None = Field(default=None)

from datetime import timedelta
from uuid import UUID

from pydantic import BaseModel, EmailStr


class TokenDecode(BaseModel):
    exp: timedelta
    sub: int 
    type: str


class TokenPayload(BaseModel):
    id: UUID


class AccessToken(BaseModel):
    access_token: str


class RefreshToken(BaseModel):
    refresh_token: str


class TokenPair(BaseModel):
    refresh: str
    access: str


class AuthenticationScheme(BaseModel):
    email: EmailStr
    password: str
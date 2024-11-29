import sys

sys.path.append('../../schemas')

from typing import Annotated
from uuid import UUID

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from repository.user import UserRepository

from app.schemas.auth import (
    AccessToken,
    AuthenticationScheme,
    RefreshToken,
    TokenPair,
    TokenPayload,
)
from app.schemas.response import ErrorResponse
from app.schemas.user import UserCreate, UserRead

from .jwt import OAUTH2_SCHEMA, JWTAuth

OAUTH2_SCHEMA = OAuth2PasswordBearer(tokenUrl="token")

class AuthService:
    _jwt_auth = JWTAuth()
    _repository = UserRepository()
    _pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    _serializer = UserRead
    
    def __verify_password(self, plain_password: str, user_password: str) -> bool:
        try:
            return self._pwd_context.verify(plain_password, user_password)
        except:
            return False
    
    def __create_password_hash(self, password: str) -> str:
        return self._pwd_context.hash(password)
    
    async def _get_by_id(self, id: str | UUID):
        result = await self._repository.get_by_condition(id=id)

        if hasattr(result, "detail"):
            return ErrorResponse(detail=result.detail, status_code=result.status_code)

        return result
    
    async def authenticate(
        self, data: AuthenticationScheme
    ) -> ErrorResponse | TokenPair:
        user = (await self._repository.get_by_condition(email=data.email)).data
        
        if not user:
            return ErrorResponse(
                detail=f"No user with email {data}",
                status_code=401,
            )
            
        if not self.__verify_password(data.password, user.password):
            return ErrorResponse(
                detail="Incorrect Password",
                status_code=401,
            )

        tokens = self._jwt_auth.create_token_pair(TokenPayload(id=str(user.id)))
        return tokens

    async def registration(self, data: UserCreate):
        data.password = self.__create_password_hash(data.password)
        user = await self._repository.create(data)
        
        if hasattr(user, "detail"):
            return ErrorResponse(detail=user.detail, status_code=user.status_code)

        return self._jwt_auth.create_token_pair(TokenPayload(id=str(user.data.id)))
        

    async def refresh(self, data: RefreshToken):
        result = self._jwt_auth.decode_token(data.refresh_token)

        if result.data.get("type") == self._jwt_auth.access_type:
            return ErrorResponse(detail="Must be refresh token", status_code=401)

        if hasattr(result, "detail"):
            return ErrorResponse(detail=result.detail, status_code=result.status_code)

        token_data = TokenPayload(id=result.data.get("sub"))
        return AccessToken(access_token=self._jwt_auth._create_access_token(token_data))
    
    async def user_by_token(self, data: AccessToken):
        payload = self._jwt_auth.decode_token(data.access_token)
        
        if hasattr(payload, "detail"):
            return ErrorResponse(detail=payload.detail, status_code=payload.status_code)

        if payload.data.get("type") == self._jwt_auth.refresh_type:
            return ErrorResponse(detail="Must be access token", status_code=401)

        result = await self._get_by_id(id=payload.data.get("sub"))
        
        if hasattr(result, "detail"):
            return ErrorResponse(detail=result.detail, status_code=result.status_code)

        return self._serializer.model_validate(result.data)


def check_auth(token: Annotated[str, Depends(OAUTH2_SCHEMA)]):
    _jwt_auth = JWTAuth()
    result = _jwt_auth.decode_token(token)
    
    if hasattr(result, "detail"):
        raise HTTPException(detail=result.detail, status_code=result.status_code)

    if result.data.get("type") == _jwt_auth.refresh_type:
        raise HTTPException(detail="Must be access token", status_code=401)

    return AccessToken(access_token=token)

auth_dependency = Depends(check_auth)
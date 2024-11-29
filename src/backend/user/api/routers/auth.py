from app.schemas.auth import (
    AccessToken,
    AuthenticationScheme,
    RefreshToken,
    TokenPair,
)
from app.schemas.response import ErrorResponse
from app.schemas.user import UserCreate, UserRead
from app.service.auth.auth import AuthService, auth_dependency
from fastapi import APIRouter, HTTPException

auth_router = APIRouter(prefix="/auth", tags=["Auth"])

service = AuthService()


@auth_router.get("/user", response_model=UserRead)
async def get_user_on_token(token: AccessToken = auth_dependency) -> UserRead:
    data = await service.user_by_token(data=token)
    
    if isinstance(data, ErrorResponse):
        raise HTTPException(detail=data.detail, status_code=data.status_code)

    return data 


@auth_router.post("/sign-in", response_model=TokenPair)
async def login(data: AuthenticationScheme) -> TokenPair:
    data = await service.authenticate(data=data)
    
    if isinstance(data, ErrorResponse):
        raise HTTPException(detail=data.detail, status_code=data.status_code)

    return data 


@auth_router.post("/sign-up", response_model=TokenPair, tags=["User"], status_code=201)
async def register(data: UserCreate) -> TokenPair:
    data = await service.registration(data=data)
    
    if isinstance(data, ErrorResponse):
        raise HTTPException(detail=data.detail, status_code=data.status_code)

    return data 


@auth_router.post("/refresh-token", response_model=AccessToken)
async def refresh_token(refresh_token: RefreshToken) -> AccessToken:
    data: AccessToken | ErrorResponse = await service.refresh(data=refresh_token)
    
    if isinstance(data, ErrorResponse):
        raise HTTPException(detail=data.detail, status_code=data.status_code)

    return data
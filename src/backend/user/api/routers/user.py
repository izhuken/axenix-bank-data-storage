from uuid import UUID

from app.schemas.response import ErrorResponse, SuccessResponse
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.service.user import UserService
from fastapi import APIRouter, HTTPException, Request

user_router = APIRouter(prefix="/user", tags=["User"])
service = UserService()


@user_router.get("/get_all")
async def get_all(
    request: Request,
    page: int = 1,
    quantity: int = 50,
    order_by: str | None = None,
):
    data = await service.get_all(
        request=request,
        page=page,
        quantity=quantity,
        order_by=order_by,
    )

    if isinstance(data, ErrorResponse):
        raise HTTPException(status_code=data.status_code, detail=data.detail)

    return data


@user_router.get("/{id}", response_model=UserRead)
async def get_by_id(id: UUID) -> UserRead:
    data = await service.get_by_id(id=id)

    if isinstance(data, ErrorResponse):
        raise HTTPException(status_code=data.status_code, detail=data.detail)

    return data


@user_router.post("/create", response_model=UserRead, status_code=201)
async def create(data: UserCreate) -> UserRead:
    data = await service.create(data=data)

    if isinstance(data, ErrorResponse):
        raise HTTPException(status_code=data.status_code, detail=data.detail)

    return data


@user_router.patch("/update/{id}", response_model=UserRead)
async def update(id: UUID, data: UserUpdate) -> UserRead:
    data = await service.update(id=id, data=data)

    if isinstance(data, ErrorResponse):
        raise HTTPException(status_code=data.status_code, detail=data.detail)

    return data


@user_router.delete("/delete/{id}", response_model=SuccessResponse)
async def delete(id: UUID) -> SuccessResponse:
    data = await service.delete(id=id)

    if isinstance(data, ErrorResponse):
        raise HTTPException(status_code=data.status_code, detail=data.detail)

    return data

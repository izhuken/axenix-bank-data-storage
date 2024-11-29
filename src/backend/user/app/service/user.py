from repository.user import UserRepository

from app.schemas.user import UserRead

from ._base_service import BaseService


class UserService(BaseService):
    _repository = UserRepository()
    _serializer = UserRead

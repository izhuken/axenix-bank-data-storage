from core.models.user import User

from ._base_sqlalchemy_repository import BaseSQLAlchemyRepository


class UserRepository(BaseSQLAlchemyRepository):
    model = User

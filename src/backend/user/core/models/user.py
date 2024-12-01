from sqlalchemy.orm import Mapped, mapped_column

from ._base import BaseModel


class User(BaseModel):
    __tablename__ = "user"

    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_admin: Mapped[bool] = mapped_column(nullable=False, default=False)
    is_superadmin: Mapped[bool] = mapped_column(nullable=False, default=False)
from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from ._base import BaseModel


class InternalReport(BaseModel):
    __tablename__ = "internal_report"

    title: Mapped[str] = mapped_column(nullable=False, unique=False)
    url: Mapped[str] = mapped_column(unique=False, nullable=False)

    user_id: Mapped[UUID] = mapped_column(nullable=False)
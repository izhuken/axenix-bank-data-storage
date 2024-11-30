from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._base import BaseModel


class InternalReport(BaseModel):
    __tablename__ = "internal_report"

    title: Mapped[str] = mapped_column(nullable=False, unique=False)
    url: Mapped[str] = mapped_column(unique=False, nullable=False)

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"),
        primary_key=True)
    user: Mapped["User"] = relationship(
    back_populates="internal_report",
    )
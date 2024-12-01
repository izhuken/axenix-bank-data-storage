from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel


class TransactionType(BaseModel):
    __tablename__ = "transaction_type"

    transaction_type_id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    transaction_type_name: Mapped[str] = mapped_column(nullable=True, unique=False)

    credit_transaction: Mapped["CreditTransaction"] = relationship(
        back_populates="transaction_type",
    )

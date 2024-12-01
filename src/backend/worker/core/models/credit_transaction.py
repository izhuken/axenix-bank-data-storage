from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel


class CreditTransaction(BaseModel):
    __tablename__ = "credit_transaction"

    transaction_id: Mapped[int] = mapped_column(
        primary_key=True, unique=True, autoincrement=True
    )
    transaction_date: Mapped[date] = mapped_column(nullable=True, unique=False)
    transaction_amount: Mapped[float] = mapped_column(nullable=True, unique=False)

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customer.customer_id", ondelete="CASCADE"), primary_key=True
    )
    credit_agreement_id: Mapped[int] = mapped_column(
        ForeignKey("credit_agreement.credit_agreement_id", ondelete="CASCADE"),
        primary_key=True,
    )
    transaction_type_id: Mapped[int] = mapped_column(
        ForeignKey("transaction_type.transaction_type_id", ondelete="CASCADE"),
        primary_key=True,
    )

    customer: Mapped["Customer"] = relationship(
        back_populates="credit_transaction",
    )
    credit_agreement: Mapped["CreditAgreement"] = relationship(
        back_populates="credit_transaction",
    )
    transaction_type: Mapped["TransactionType"] = relationship(
        back_populates="credit_transaction",
    )

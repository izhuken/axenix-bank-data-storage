from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel


class CreditAgreement(BaseModel):
    __tablename__ = "credit_agreement"

    credit_agreement_id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    agreement_date: Mapped[date] = mapped_column(nullable=True, unique=False)
    loan_amount: Mapped[float] = mapped_column(nullable=True, unique=False)
    loan_term: Mapped[int] = mapped_column(nullable=True, unique=False)
    interest_rate: Mapped[float] = mapped_column(nullable=True, unique=False)

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customer.customer_id", ondelete="CASCADE"), primary_key=True
    )
    credit_product_id: Mapped[int] = mapped_column(
        ForeignKey("credit_product.credit_product_id", ondelete="CASCADE"),
        primary_key=True,
    )

    customer: Mapped["Customer"] = relationship(
        back_populates="credit_agreement",
    )
    credit_product: Mapped["CreditProduct"] = relationship(
        back_populates="credit_agreement",
    )
    credit_transaction: Mapped["CreditTransaction"] = relationship(
        back_populates="credit_agreement",
    )

    fact: Mapped["Fact"] = relationship(
        back_populates="credit_agreement",
    )

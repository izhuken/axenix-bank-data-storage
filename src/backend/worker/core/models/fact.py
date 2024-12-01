from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel


class Fact(BaseModel):
    __tablename__ = "fact"

    # из agreement - loan_amount
    credit_sum: Mapped[float] = mapped_column(primary_key=True, unique=False)
    # sum платежек юзера
    payment_amount: Mapped[float] = mapped_column(nullable=True, unique=False)
    # count платежек юзера
    made_payments: Mapped[int] = mapped_column(nullable=True, unique=False)
    # из agreement - loan_term
    calculated_payment_number: Mapped[float] = mapped_column(
        nullable=True, unique=False
    )
    # выч сам
    is_closed: Mapped[bool] = mapped_column(nullable=True, unique=False)
    # из agreement - credit_agreement_id
    contract_number: Mapped[int] = mapped_column(nullable=True, unique=True)
    # из agreement - agreement_date
    created_at: Mapped[date] = mapped_column(nullable=True, unique=False)
    # из agreement - transaction - дата последнего платежа
    closed_at: Mapped[date] = mapped_column(nullable=True, unique=False)

    user_name: Mapped[str] = mapped_column(nullable=True, unique=False)
    user_tin: Mapped[str] = mapped_column(nullable=True, unique=False)
    user_phone: Mapped[str] = mapped_column(nullable=True, unique=False)

    # из agreement - credit_agreement_id
    contract_id: Mapped[int] = mapped_column(
        ForeignKey("credit_agreement.credit_agreement_id", ondelete="CASCADE"),
        primary_key=True,
        unique=True,
    )
    # из customer_id - customer_id
    user_id: Mapped[int] = mapped_column(
        ForeignKey("customer.customer_id", ondelete="CASCADE"), primary_key=True
    )

    user: Mapped["Customer"] = relationship(
        back_populates="fact",
    )
    credit_agreement: Mapped["CreditAgreement"] = relationship(
        back_populates="fact",
    )

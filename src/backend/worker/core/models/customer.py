from datetime import date

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel


class Customer(BaseModel):
    __tablename__ = "customer"

    customer_id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    customer_type_id: Mapped[int] = mapped_column(nullable=True, unique=False)
    name: Mapped[str] = mapped_column(nullable=True, unique=False)
    date_of_birth: Mapped[date] = mapped_column(nullable=True, unique=False)
    registration_date: Mapped[date] = mapped_column(nullable=True, unique=False)
    tin: Mapped[str] = mapped_column(nullable=True, unique=False)
    contact_info: Mapped[str] = mapped_column(nullable=True, unique=False)

    credit_agreement: Mapped["CreditAgreement"] = relationship(
        back_populates="customer",
    )
    credit_transaction: Mapped["CreditTransaction"] = relationship(
        back_populates="customer",
    )
    fact: Mapped["Fact"] = relationship(
        back_populates="user",
    )

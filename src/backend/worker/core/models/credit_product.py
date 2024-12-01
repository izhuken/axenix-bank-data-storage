from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel


class CreditProduct(BaseModel):
    __tablename__ = "credit_product"

    credit_product_id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    product_name: Mapped[str] = mapped_column(nullable=True, unique=False)
    interest_rate: Mapped[float] = mapped_column(nullable=True, unique=False)
    max_loan_amount: Mapped[float] = mapped_column(nullable=True, unique=False)
    min_repayment_term: Mapped[int] = mapped_column(nullable=True, unique=False)
    collateral_required: Mapped[bool] = mapped_column(nullable=True, unique=False)

    credit_agreement: Mapped["CreditAgreement"] = relationship(
        back_populates="credit_product",
    )

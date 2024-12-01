from datetime import date

from pydantic import Field

from ._base import BaseSchema


class SearchRequest(BaseSchema):
    credit_sum_from: float | None = Field(default=None)
    credit_sum_to: float | None = Field(default=None)
    made_payments_from: float | None = Field(default=None)
    made_payments_to: float | None = Field(default=None)
    calculated_payment_number_from: int | None = Field(default=None)
    calculated_payment_number_to: int | None = Field(default=None)
    is_closed: bool
    closed_at_from: date | None = Field(default=None)
    closed_at_to: date | None = Field(default=None)
    contract_number: int | None = Field(default=None)
    created_at_from: date | None = Field(default=None)
    created_at_to: date | None = Field(default=None)
    action_type: str
    target_field: str


class SearchResponse(BaseSchema):
    target_value: float
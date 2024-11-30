from datetime import date

from ._base import BaseSchema


class SearchRequest(BaseSchema):
    credit_sum_from: float
    credit_sum_to: float
    made_payments_from: float
    made_payments_to: float
    payment_number_from: int
    payment_number_to: int
    calculated_payment_number_from: int
    calculated_payment_number_to: int
    is_closed: bool
    closed_at_from: date
    closed_at_to: date
    contract_number: int
    create_at_from: date
    create_at_to: date
    action_type: str
    target_field: str


class SearchResponse(BaseSchema):
    target_value: int
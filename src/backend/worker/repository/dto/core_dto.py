from dataclasses import dataclass
from typing import Literal


@dataclass
class CommandDTO:
    command: str
    payload: dict


@dataclass
class CreateCustomerPayload:
    name: str
    date_of_birth: str | None
    registration_date: str
    tin: str
    contact_info: str


@dataclass
class TaskTransactionPayload:
    customer_name: str
    agreement_type: str
    transfer_type: str
    transaction_date: str
    transaction_amount: str


@dataclass
class ApproveCreditPayload:
    customer_name: str
    agreement_number: str
    credit_product_type: str
    agreement_date: str
    loan_amount: int | float
    loan_tern: int | float


class CreateCustomerCommand(CommandDTO):
    command: Literal["create_customer_task"]
    payload: CreateCustomerPayload


class CreateTransactionCommand(CommandDTO):
    command: Literal["create_transaction_task"]
    payload: TaskTransactionPayload


class ApproveCreditCommand(CommandDTO):
    command: Literal["approve_credit_task"]
    payload: ApproveCreditPayload

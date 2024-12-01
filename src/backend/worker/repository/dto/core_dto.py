from dataclasses import dataclass
from typing import Literal


@dataclass
class CommandDTO:
    command: str
    payload: dict


@dataclass
class CreateCustomerPayload:
    customer_type_id: int
    name: str
    date_of_birth: str
    registration_date: str
    tin: str
    contact_info: str


@dataclass
class TaskTransactionPayload:
    user_id: str
    report: str


@dataclass
class ApproveCreditPayload:
    customer_name: str
    agreement_number: str
    credit_product_type: str
    agreement_date: str
    loan_amount: int | float
    loan_tern: int | float


@dataclass
class InitPayload:
    customer_agreement: str
    credit_products: str
    credit_transactions: str
    customers: str
    transaction_types: str


class CreateCustomerCommand(CommandDTO):
    command: Literal["create_customer_task"]
    payload: CreateCustomerPayload


class CreateTransactionCommand(CommandDTO):
    command: Literal["create_transaction_task"]
    payload: TaskTransactionPayload


class ApproveCreditCommand(CommandDTO):
    command: Literal["approve_credit_task"]
    payload: ApproveCreditPayload


class InitCommand(CommandDTO):
    command: Literal["init_task"]
    payload: InitPayload

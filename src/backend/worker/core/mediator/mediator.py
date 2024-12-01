from dataclasses import dataclass

from repository.dto import CreateCustomerPayload, InitPayload, TaskTransactionPayload

from core.listener import (
    ApproveCreditTaskListener,
    CustomerCreationListener,
    InitTaskListener,
    TransactionCreationTaskListener,
)


@dataclass
class MediatorCommand:
    command: str
    payload: dict


class Mediator:
    create_transaction_listener = TransactionCreationTaskListener()
    approve_credit_listener = ApproveCreditTaskListener()
    create_user_listener = CustomerCreationListener()
    init_listener = InitTaskListener()

    async def notify(self, command: MediatorCommand):
        print("Command received: ", command)

        if command.command == "create_transaction_task":
            command.payload = TaskTransactionPayload(**command.payload)
            return await self.create_transaction_listener.receive(command)

        if command.command == "create_customer_task":
            command.payload = CreateCustomerPayload(**command.payload)
            return await self.create_user_listener.receive(command)

        if command.command == "init_task":
            command.payload = InitPayload(**command.payload)
            return await self.init_listener.receive(command)

        return

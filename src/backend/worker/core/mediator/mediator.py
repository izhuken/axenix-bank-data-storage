from dataclasses import dataclass

from repository.dto import InitPayload, TaskTransactionPayload

from core.listener import (
    ApproveCreditTaskListener,
    InitTaskListener,
    TransactionCreationTaskListener,
    UserCreationListener,
)


@dataclass
class MediatorCommand:
    command: str
    payload: dict


class Mediator:
    create_transaction_listener = TransactionCreationTaskListener()
    approve_credit_listener = ApproveCreditTaskListener()
    create_user_listener = UserCreationListener()
    init_listener = InitTaskListener()

    async def notify(self, command: MediatorCommand):
        if command.command == "create_transaction_task":
            command.payload = TaskTransactionPayload(**command.payload)
            return await self.create_transaction_listener.receive(command)

        if command.command == "approve_credit_task":
            return await self.approve_credit_listener.receive(command)

        if command.command == "create_transaction_task":
            return await self.create_transaction_listener.receive(command)

        if command.command == "init_task":
            command.payload = InitPayload(**command.payload)
            return await self.init_listener.receive(command)

        return

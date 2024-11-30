from dataclasses import dataclass

from core.listener import (
    ApproveCreditTaskListener,
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

    async def notify(self, command: MediatorCommand):
        if command.command == "create_transaction_task":
            return await self.create_transaction_listener.receive(command.payload)

        if command.command == "approve_credit_task":
            return await self.approve_credit_listener.receive(command.payload)

        if command.command == "create_transaction_task":
            return await self.create_transaction_listener.receive(command.payload)

        return

from repository.dto import CreateCustomerPayload

from .interface import IListener


class UserCreationListener(IListener):
    async def receive(command: CreateCustomerPayload):
        print(command)

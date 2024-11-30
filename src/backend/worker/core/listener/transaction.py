from repository.dto import CreateTransactionCommand

from .interface import IListener


class TransactionCreationTaskListener(IListener):
    async def receive(command: CreateTransactionCommand):
        print(command)

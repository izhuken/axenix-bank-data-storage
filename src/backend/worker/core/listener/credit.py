from repository.dto import ApproveCreditCommand

from .interface import IListener


class ApproveCreditTaskListener(IListener):
    async def receive(self, command: ApproveCreditCommand):
        print(command)

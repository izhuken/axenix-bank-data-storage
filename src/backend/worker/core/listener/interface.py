from abc import ABC

from repository.dto import CommandDTO


class IListener(ABC):
    async def receive(command: CommandDTO):
        raise NotImplementedError()

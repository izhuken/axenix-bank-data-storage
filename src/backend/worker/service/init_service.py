from repository.dto import InitPayload


class InitService:
    async def process(payload: InitPayload):
        """
        Алгоритм:
        1. преобразовать кастомеров и выгрузить в базу
        2. преобразовать типы транзакций и выгрузить в базу
        3. преобразовать credit products и выгрузить в базу
        4. преобразовать credit agreements и выгрузить в базу
        5. преобразовать credit transactions и выгрузить в базу
        """
        return

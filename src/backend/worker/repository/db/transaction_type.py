from core.models import TransactionType
from core.settings import SESSION
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from repository.dto import ErrorDTO, SuccessDTO


class TransactionTypeRepository:
    async def get_by_condition(
        self, **kwargs
    ) -> SuccessDTO[list[TransactionType]] | ErrorDTO[str | int]:
        query = select(TransactionType)

        for key, value in kwargs.items():
            query = query.filter(getattr(TransactionType, key) == value).limit(1)

        try:
            async with SESSION() as session:
                result = await session.execute(query)
                data = result.scalars().all()
                return SuccessDTO[list[TransactionType]](data)
        except IntegrityError as e:
            print(e)
            return ErrorDTO("Data already exists", 400)

    async def create(
        self, data: list[dict]
    ) -> SuccessDTO[TransactionType] | ErrorDTO[str | int]:
        try:
            async with SESSION() as session:
                inserted_data = []
                for insert_data in data:
                    new_transaction_type = TransactionType(**insert_data)
                    session.add(new_transaction_type)
                    inserted_data.append(new_transaction_type)
                await session.commit()
                return SuccessDTO[TransactionType](inserted_data)
        except IntegrityError as e:
            print(e)
            return ErrorDTO("Data already exists", 400)

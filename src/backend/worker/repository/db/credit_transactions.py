from core.models import CreditTransaction
from core.settings import SESSION
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from repository.dto import ErrorDTO, SuccessDTO


class CreditTransactionRepository:
    async def get_by_condition(
        self, **kwargs
    ) -> SuccessDTO[CreditTransaction] | ErrorDTO[str | int]:
        query = select(CreditTransaction)

        for key, value in kwargs.items():
            query = query.filter(getattr(CreditTransaction, key) == value)

        try:
            async with SESSION() as session:
                result = await session.execute(query)
                data = result.scalars().all()
                return SuccessDTO[list[CreditTransaction]](data)
        except IntegrityError as e:
            print(e)
            return ErrorDTO("Data already exists", 400)

    async def create(
        self, data: list[dict]
    ) -> SuccessDTO[CreditTransaction] | ErrorDTO[str | int]:
        try:
            async with SESSION() as session:
                for insert_data in data:
                    new_transaction_type = CreditTransaction(**insert_data)
                    session.add(new_transaction_type)
                await session.commit()
                return SuccessDTO[bool](True)
        except IntegrityError as e:
            print(e)
            return ErrorDTO("Data already exists", 400)

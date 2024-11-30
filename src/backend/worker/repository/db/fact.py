from core.models import CreditTransaction, Fact
from core.settings import SESSION
from sqlalchemy import func, select, update
from sqlalchemy.exc import IntegrityError

from repository.dto import ErrorDTO, SuccessDTO


class FactRepository:
    async def get_by_condition(
        self, **kwargs
    ) -> SuccessDTO[Fact] | ErrorDTO[str | int]:
        query = select(Fact)

        for key, value in kwargs.items():
            query = query.filter(getattr(Fact, key) == value).limit(1)

        try:
            async with SESSION() as session:
                result = await session.execute(query)
                data = result.scalars().all()
                return SuccessDTO[Fact](data)
        except IntegrityError as e:
            print(e)
            return ErrorDTO("Data already exists", 400)

    async def create(self, data: dict) -> SuccessDTO[Fact] | ErrorDTO[str | int]:
        try:
            async with SESSION() as session:
                new_transaction_type = Fact(**data)
                session.add(new_transaction_type)
                await session.commit()
                return SuccessDTO[bool](True)
        except IntegrityError as e:
            print(e)
            return ErrorDTO("Data already exists", 400)

    async def update_with_transaction(
        self, fact_id, fact_upload_payload: dict, new_transaction_payload: dict
    ):
        try:
            async with SESSION() as session:
                count_query = select(func.count(CreditTransaction.id))
                transaction_count = (await session.execute(count_query)).scalar()
                print(transaction_count)
                new_transaction_payload["transaction_id"] = transaction_count + 1
                session.add(CreditTransaction(**new_transaction_payload))
                query = (
                    update(Fact).where(Fact.id == fact_id).values(**fact_upload_payload)
                )
                await session.execute(query)
                await session.commit()
        except IntegrityError as e:
            print(e)
            return ErrorDTO("", 400)

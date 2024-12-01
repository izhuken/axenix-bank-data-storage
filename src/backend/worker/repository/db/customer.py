from core.models import Customer
from core.settings import SESSION
from sqlalchemy import func, select
from sqlalchemy.exc import IntegrityError

from repository.dto import ErrorDTO, SuccessDTO


class CustomerRepository:
    async def new_customer(
        self, data: dict
    ) -> SuccessDTO[Customer] | ErrorDTO[str | int]:
        try:
            async with SESSION() as session:
                query_count = select(func.count(Customer.id))
                count = (await session.execute(query_count)).scalar()
                data["customer_id"] = count + 1
                new_customer = Customer(**data)
                session.add(new_customer)
                await session.commit()
                return SuccessDTO[Customer](True)
        except IntegrityError as e:
            print(e)
            return ErrorDTO("Data already exists", 400)

    async def create(
        self, data: list[dict]
    ) -> SuccessDTO[Customer] | ErrorDTO[str | int]:
        try:
            async with SESSION() as session:
                for insert_data in data:
                    new_transaction_type = Customer(**insert_data)
                    session.add(new_transaction_type)
                await session.commit()
                return SuccessDTO[bool](True)
        except IntegrityError as e:
            print(e)
            return ErrorDTO("Data already exists", 400)

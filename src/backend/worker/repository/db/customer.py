from core.models import Customer
from core.settings import SESSION
from sqlalchemy.exc import IntegrityError

from repository.dto import ErrorDTO, SuccessDTO


class CustomerRepository:
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

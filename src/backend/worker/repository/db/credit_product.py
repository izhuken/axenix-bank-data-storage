from core.models import CreditProduct
from core.settings import SESSION
from sqlalchemy.exc import IntegrityError

from repository.dto import ErrorDTO, SuccessDTO


class CreditProductRepository:
    async def create(
        self, data: list[dict]
    ) -> SuccessDTO[CreditProduct] | ErrorDTO[str | int]:
        try:
            async with SESSION() as session:
                for insert_data in data:
                    new_transaction_type = CreditProduct(**insert_data)
                    session.add(new_transaction_type)
                await session.commit()
                return SuccessDTO[bool](True)
        except IntegrityError as e:
            print(e)
            return ErrorDTO("Data already exists", 400)

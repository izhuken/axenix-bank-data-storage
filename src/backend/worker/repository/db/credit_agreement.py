from core.models import CreditAgreement
from core.settings import SESSION
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload

from repository.dto import ErrorDTO, SuccessDTO


class CreditAgreementRepository:
    async def get_all(self, limit, offset):
        query = (
            select(CreditAgreement)
            .options(joinedload(CreditAgreement.customer))
            .limit(limit)
            .offset(offset)
        )

        try:
            async with SESSION() as session:
                result = await session.execute(query)
                data = result.scalars().all()
                return SuccessDTO[list[CreditAgreement]](data)
        except IntegrityError as e:
            print(e)
            return ErrorDTO("Data already exists", 400)

        pass

    async def create(
        self, data: list[dict]
    ) -> SuccessDTO[CreditAgreement] | ErrorDTO[str | int]:
        try:
            async with SESSION() as session:
                for insert_data in data:
                    new_transaction_type = CreditAgreement(**insert_data)
                    session.add(new_transaction_type)
                await session.commit()
                return SuccessDTO[bool](True)
        except IntegrityError as e:
            print(e)
            return ErrorDTO("Data already exists", 400)

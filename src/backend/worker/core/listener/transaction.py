import datetime

import pandas as pd
from repository.db import (
    CreditTransactionRepository,
    FactRepository,
    TransactionTypeRepository,
)
from repository.dto import CreateTransactionCommand
from service.elastic_service import ElasticSearchService

from core.settings.elastic import _es
from core.settings.s3 import minio_client
from core.settings.settings import S3_BUCKET_NAME

from .interface import IListener


class TransactionCreationTaskListener(IListener):
    fact_repository = FactRepository()
    transaction_repository = CreditTransactionRepository()
    transaction_type_repository = TransactionTypeRepository()
    elastic_service = ElasticSearchService(_es, "fact", "fact")

    async def receive(self, command: CreateTransactionCommand):
        data = minio_client.get_object(S3_BUCKET_NAME, command.payload.report)
        df = pd.read_csv(data)

        print(df)

        for chunk in self.iterate_in_chunks(df, 100):
            for _, row in chunk.iterrows():
                transfer_types_data = (
                    await self.transaction_type_repository.get_by_condition(
                        transaction_type_name=row.get("transfer_type")
                    )
                )

                if not transfer_types_data.data or len(transfer_types_data.data) == 0:
                    continue

                fact_data = await self.fact_repository.get_by_condition(
                    contract_number=row.get("agreement_number"),
                )

                if not fact_data.data or len(fact_data.data) == 0:
                    continue

                fact = fact_data.data[0]
                transfer_type = transfer_types_data.data[0]

                fact_upd = {
                    "payment_amount": fact.payment_amount
                    + float(row.get("transaction_amount")),
                    "made_payments": fact.made_payments + 1,
                }

                if (
                    fact.payment_amount + float(row.get("transaction_amount"))
                    >= fact.credit_sum
                ):
                    fact_upd["is_closed"] = True
                    fact_upd["closed_at"] = datetime.datetime.strptime(
                        str(row.get("transaction_date")), "%Y-%m-%d"
                    ).date()

                updated_fact = await self.fact_repository.update_with_transaction(
                    fact.id,
                    fact_upd,
                    {
                        "transaction_date": datetime.datetime.strptime(
                            str(row.get("transaction_date")), "%Y-%m-%d"
                        ).date(),
                        "transaction_amount": float(row.get("transaction_amount")),
                        "customer_id": int(fact.user_id),
                        "credit_agreement_id": int(fact.contract_id),
                        "transaction_type_id": int(transfer_type.transaction_type_id),
                    },
                )

                if not hasattr(updated_fact, "data"):
                    return

                elastic_payload = {
                    "credit_sum": updated_fact.data.credit_sum,
                    "payment_amount": updated_fact.data.payment_amount,
                    "made_payments": updated_fact.data.made_payments,
                    "calculated_payment_number": updated_fact.data.calculated_payment_number,
                    "is_closed": updated_fact.data.is_closed,
                    "contract_number": updated_fact.data.contract_number,
                    "created_at": updated_fact.data.created_at,
                    "closed_at": updated_fact.data.closed_at,
                    "contract_id": updated_fact.data.contract_id,
                    "user_id": updated_fact.data.user_id,
                    "user_name": updated_fact.data.user_name,
                    "user_tin": updated_fact.data.user_tin,
                    "user_phone": updated_fact.data.user_phone,
                    "id_fact": updated_fact.data.id,
                }

                self.elastic_service.update_data(elastic_payload)

    def iterate_in_chunks(self, dataframe: pd.DataFrame, chunk_size: int):
        for start in range(0, len(dataframe), chunk_size):
            end = start + chunk_size
            yield dataframe.iloc[start:end]

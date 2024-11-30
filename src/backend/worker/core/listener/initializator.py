import datetime
from time import time

import pandas as pd
from repository.db import (
    CreditAgreementRepository,
    CreditProductRepository,
    CreditTransactionRepository,
    CustomerRepository,
    FactRepository,
    TransactionTypeRepository,
)
from repository.dto import CreateTransactionCommand

from core.models import CreditAgreement
from core.settings.s3 import minio_client
from core.settings.settings import S3_BUCKET_NAME

from .interface import IListener


class InitTaskListener(IListener):
    customer_repo = CustomerRepository()
    credit_product_repo = CreditProductRepository()
    transaction_type_repo = TransactionTypeRepository()
    credit_agreement_repo = CreditAgreementRepository()
    credit_transaction_repo = CreditTransactionRepository()
    fact_repository = FactRepository()

    async def receive(self, _: CreateTransactionCommand):
        await self._create_transaction_types()
        await self._create_customers()
        await self._create_credit_products()
        await self._create_credit_agreement()
        await self._create_credit_transactions()
        await self._create_fact_table()

    async def _create_fact_table(self):
        start = time()

        for counter in range(100, 2600, 100):
            agreements = await self.credit_agreement_repo.get_all(100, counter - 100)

            for agreement in agreements.data:
                await self.__create_fact(agreement)

        print("finish")

        print(time() - start)

    async def __create_fact(self, agreement: CreditAgreement):
        transactions = (
            await self.credit_transaction_repo.get_by_condition(
                credit_agreement_id=agreement.credit_agreement_id
            )
        ).data

        payment_amount = sum(
            [transaction.transaction_amount for transaction in transactions]
        )
        made_payments = len(transactions)
        is_closed = payment_amount == agreement.loan_amount

        fact = {
            "credit_sum": float(agreement.loan_amount),
            "payment_amount": float(payment_amount),
            "made_payments": int(made_payments),
            "calculated_payment_number": float(agreement.loan_term),
            "is_closed": is_closed,
            "contract_number": int(agreement.credit_agreement_id),
            "created_at": agreement.agreement_date,
            "closed_at": None if not is_closed else transactions[-1].transaction_date,
            "contract_id": int(agreement.credit_agreement_id),
            "user_id": int(agreement.customer_id),
            "user_name": agreement.customer.name,
            "user_tin": agreement.customer.tin,
            "user_phone": agreement.customer.contact_info,
        }

        await self.fact_repository.create(fact)

    async def _create_credit_transactions(self):
        data = minio_client.get_object(S3_BUCKET_NAME, "CreditTransactions.csv")
        df = pd.read_csv(data)

        for chunk in self.iterate_in_chunks(df, 100):
            payload = []

            for _, row in chunk.iterrows():
                payload.append(
                    {
                        "transaction_id": int(row.get("TransactionID")),
                        "transaction_date": datetime.datetime.strptime(
                            str(row.get("TransactionDate")), "%Y-%m-%d"
                        ).date(),
                        "transaction_amount": float(row.get("TransactionAmount")),
                        "customer_id": int(row.get("CustomerID")),
                        "credit_agreement_id": int(row.get("CreditAgreementID")),
                        "transaction_type_id": int(row.get("TransactionTypeID")),
                    }
                )

            await self.credit_transaction_repo.create(payload)

    async def _create_credit_agreement(self):
        data = minio_client.get_object(S3_BUCKET_NAME, "CreditAgreements.csv")
        df = pd.read_csv(data)

        for chunk in self.iterate_in_chunks(df, 100):
            payload = []

            for _, row in chunk.iterrows():
                payload.append(
                    {
                        "credit_agreement_id": row.get("CreditAgreementID"),
                        "agreement_date": datetime.datetime.strptime(
                            str(row.get("AgreementDate")), "%Y-%m-%d"
                        ).date(),
                        "loan_amount": float(row.get("LoanAmount")),
                        "loan_term": int(row.get("LoanTerm")),
                        "interest_rate": float(row.get("InterestRate")),
                        "customer_id": int(row.get("CustomerID")),
                        "credit_product_id": int(row.get("CreditProductID")),
                    }
                )

            await self.credit_agreement_repo.create(payload)

    async def _create_credit_products(self):
        data = minio_client.get_object(S3_BUCKET_NAME, "CreditProducts.csv")
        df = pd.read_csv(data)

        payload = []

        for _, row in df.iterrows():
            payload.append(
                {
                    "credit_product_id": row.get("CreditProductID"),
                    "product_name": row.get("ProductName"),
                    "interest_rate": row.get("InterestRate"),
                    "max_loan_amount": float(row.get("MaxLoanAmount")),
                    "min_repayment_term": int(row.get("MinRepaymentTerm")),
                    "collateral_required": True
                    if row.get("CollateralRequired") == "Да"
                    else False,
                }
            )

        return await self.credit_product_repo.create(payload)

    async def _create_transaction_types(self):
        data = minio_client.get_object(S3_BUCKET_NAME, "TransactionTypes.csv")
        df = pd.read_csv(data)
        payload = []

        for _, row in df.iterrows():
            payload.append(
                {
                    "transaction_type_id": row.get("TransactionTypeID"),
                    "transaction_type_name": row.get("TransactionTypeName"),
                }
            )

        created_transactions = await self.transaction_type_repo.create(payload)

        return [
            {
                "transaction_type_id": item.transaction_type_id,
                "transaction_type_name": item.transaction_type_name,
                "id": item.id,
            }
            for item in created_transactions.data
        ]

    async def _create_customers(self):
        data = minio_client.get_object(S3_BUCKET_NAME, "Customers.csv")
        df = pd.read_csv(data)

        for chunk in self.iterate_in_chunks(df, 100):
            payload = []

            for _, row in chunk.iterrows():
                payload.append(
                    {
                        "customer_id": row.get("CustomerID"),
                        "customer_type_id": row.get("CustomerTypeID"),
                        "name": row.get("Name"),
                        "date_of_birth": datetime.datetime.strptime(
                            str(row.get("DateOfBirth")), "%Y-%m-%d"
                        ).date()
                        if str(row.get("DateOfBirth")) != "nan"
                        else None,
                        "registration_date": datetime.datetime.strptime(
                            str(row.get("RegistrationDate")), "%Y-%m-%d"
                        ).date()
                        if str(row.get("RegistrationDate")) != "nan"
                        else None,
                        "tin": str(row.get("TIN")),
                        "contact_info": str(row.get("ContactInfo")),
                    }
                )

            await self.customer_repo.create(payload)

    def iterate_in_chunks(self, dataframe: pd.DataFrame, chunk_size: int):
        for start in range(0, len(dataframe), chunk_size):
            end = start + chunk_size
            yield dataframe.iloc[start:end]

from datetime import datetime

from repository.db import CustomerRepository
from repository.dto import CreateCustomerCommand

from .interface import IListener


class CustomerCreationListener(IListener):
    customer_repository = CustomerRepository()

    async def receive(self, command: CreateCustomerCommand):
        create_user_payload = command.payload.__dict__
        create_user_payload["registration_date"] = datetime.strptime(
            str(create_user_payload["registration_date"]), "%Y-%m-%d"
        ).date()
        create_user_payload["date_of_birth"] = datetime.strptime(
            str(create_user_payload["date_of_birth"]), "%Y-%m-%d"
        ).date()
        return await self.customer_repository.new_customer(command.payload.__dict__)

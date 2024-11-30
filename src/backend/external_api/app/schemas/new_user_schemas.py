from datetime import date
from enum import Enum

from ._base import BaseSchema


class CustomerTypeEnum(Enum):
    individual: int = 1
    legal_entity: int = 2

class CreateCustomerRequest(BaseSchema):
    customer_type_id: CustomerTypeEnum
    name: str
    date_of_birth: date
    registration_date: date
    tin: str
    contact_info: str
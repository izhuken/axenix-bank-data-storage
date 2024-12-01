from datetime import date
from uuid import uuid4

ELASTIC_MODEL = {
    "credit_sum": float(),
    "payment_amount": float(),
    "made_payments": int(),
    "calculated_payment_number": float(),
    "is_closed": bool(),
    "contract_number": int(),
    "created_at": date.today(),
    "closed_at": date.today(),
    "contract_id": int(),
    "user_id": int(),
    "user_name": str(),
    "user_tin": str(),
    "user_phone": str(),
    "id_fact": uuid4(),
}

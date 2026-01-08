from pydantic import BaseModel
from datetime import date
from typing import Optional

class ExpenseBase(BaseModel):
    expense_date: date
    category: str
    amount: float
    description: Optional[str] = None
    payment_mode: str
    merchant_name: str
    location: Optional[str] = None
    notes: Optional[str] = None
    created_by: str

class ExpenseCreate(ExpenseBase):
    pass

class ExpenseResponse(ExpenseBase):
    expense_id: str

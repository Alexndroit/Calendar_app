from pydantic import BaseModel, EmailStr
from typing import Optional

class CustomerCreate(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int] = None  # Assuming age is optional in your logic.

class Customer(CustomerCreate):
    id: int

    class Config:
        orm_mode = True

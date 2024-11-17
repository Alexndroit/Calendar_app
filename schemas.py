from pydantic import BaseModel
from typing import List, Optional

# Schema for Address
class AddressBase(BaseModel):
    street: str
    city: str
    zip_code: str

class AddressCreate(AddressBase):
    pass

class Address(AddressBase):
    id: int
    customer_id: int

    class Config:
        orm_mode = True

# Schema for Customer
class CustomerBase(BaseModel):
    name: str
    email: str

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int
    addresses: List[Address] = []

    class Config:
        orm_mode = True

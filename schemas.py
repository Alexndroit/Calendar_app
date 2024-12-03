from pydantic import BaseModel, Field
from typing import List

# Schema for Address
class AddressBase(BaseModel):
    street: str = Field(..., max_length=200)
    city: str = Field(..., max_length=100)
    zip_code: int = Field(..., ge=10000, le=99999)  # For US 5-digit ZIP codes

class AddressCreate(AddressBase):
    pass

class Address(AddressBase):
    id: int
    customer_id: int

    class Config:
        orm_mode = True

# Schema for Customer
class CustomerBase(BaseModel):
    name: str = Field(..., max_length=100)
    email: str = Field(
        ...,
        max_length=100,
        pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    )
    age: int = Field(..., ge=18, le=100)  # Valid age range

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int
    addresses: List[Address] = []

    class Config:
        orm_mode = True

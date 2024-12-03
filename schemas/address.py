from pydantic import BaseModel, Field

class AddressCreate(BaseModel):
    street: str
    city: str
    zip_code: str = Field(..., pattern=r"^\d+$", description="ZIP code must contain only numbers.")

class Address(AddressCreate):
    id: int
    customer_id: int

    class Config:
        orm_mode = True

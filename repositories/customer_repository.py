from sqlalchemy.orm import Session
from typing import List, Optional
from models.customer import Customer as CustomerModel
from schemas.customer import CustomerCreate

class CustomerRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, customer: CustomerCreate) -> CustomerModel:
        new_customer = CustomerModel(**customer.dict())
        self.db.add(new_customer)
        self.db.commit()
        self.db.refresh(new_customer)
        return new_customer

    def get(self, customer_id: int) -> Optional[CustomerModel]:
        return self.db.query(CustomerModel).filter(CustomerModel.id == customer_id).first()

    def list(self, offset: int = 0, limit: int = 10) -> List[CustomerModel]:
        return self.db.query(CustomerModel).offset(offset).limit(limit).all()

    def update(self, customer: CustomerModel, updated_customer: CustomerCreate) -> CustomerModel:
        for field, value in updated_customer.dict(exclude_unset=True).items():
            setattr(customer, field, value)
        self.db.commit()
        self.db.refresh(customer)
        return customer

    def delete(self, customer: CustomerModel) -> None:
        self.db.delete(customer)
        self.db.commit()

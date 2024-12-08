from sqlalchemy.orm import Session
from typing import List
from models.address import Address
from schemas.address import AddressCreate

class AddressRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, address_data: AddressCreate, customer_id: int) -> Address:
        new_address = Address(**address_data.dict(), customer_id=customer_id)
        with self.db.begin():
            self.db.add(new_address)
        return new_address

    def list_by_customer(self, customer_id: int) -> List[Address]:
        return self.db.query(Address).filter(Address.customer_id == customer_id).all()

    def list(self) -> List[Address]:
        return self.db.query(Address).all()

    def get(self, customer_id: int, address_id: int) -> Address:
        return self.db.query(Address).filter(Address.customer_id == customer_id, Address.id == address_id).first()

    def update(self, address_id: int, address_data: AddressCreate) -> Address:
        address = self.db.query(Address).filter(Address.id == address_id).first()
        if address:
            address.street = address_data.street
            address.city = address_data.city
            address.zip_code = address_data.zip_code
            self.db.commit()
            return address
        return None

    def delete(self, address: Address) -> None:
        self.db.delete(address)
        self.db.commit()

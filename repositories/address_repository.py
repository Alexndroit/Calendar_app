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

    def update_bulk(self, customer_id: int, new_addresses: List[AddressCreate]) -> List[Address]:
        # Fetch current addresses for the customer
        existing_addresses = self.db.query(Address).filter(Address.customer_id == customer_id).all()
        existing_map = {f"{addr.street}|{addr.city}|{addr.zip_code}": addr for addr in existing_addresses}

        # Keep track of updated addresses
        updated_addresses = []

        # Step 1: Update existing or add new addresses
        for address_data in new_addresses:
            key = f"{address_data.street}|{address_data.city}|{address_data.zip_code}"
            if key in existing_map:
                # Update existing address
                existing_address = existing_map[key]
                existing_address.street = address_data.street
                existing_address.city = address_data.city
                existing_address.zip_code = address_data.zip_code
                updated_addresses.append(existing_address)
                del existing_map[key]  # Remove from map as it's processed
            else:
                # Add new address
                new_address = Address(customer_id=customer_id, **address_data.dict())
                updated_addresses.append(new_address)

        # Step 2: Delete addresses that were not in the incoming list
        for address_to_delete in existing_map.values():
            self.db.delete(address_to_delete)

        # Commit changes to the database
        self.db.add_all(updated_addresses)
        self.db.commit()

        # Return updated list of addresses
        return self.db.query(Address).filter(Address.customer_id == customer_id).all()

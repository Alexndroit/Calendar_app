from sqlalchemy.orm import Session
from . import models, schemas

# Create a new customer
def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(name=customer.name, email=customer.email)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

# Get a customer by ID
def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()

# Get all customers
def get_customers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Customer).offset(skip).limit(limit).all()

# Update an existing customer
def update_customer(db: Session, db_customer: models.Customer, updated_customer: schemas.CustomerCreate):
    db_customer.name = updated_customer.name
    db_customer.email = updated_customer.email
    db.commit()
    db.refresh(db_customer)
    return db_customer

# Delete a customer by ID
def delete_customer(db: Session, db_customer: models.Customer):
    db.delete(db_customer)
    db.commit()

# Create a new address
def create_address(db: Session, address: schemas.AddressCreate, customer_id: int):
    db_address = models.Address(**address.dict(), customer_id=customer_id)
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address

# Get all addresses for a customer
def get_addresses_by_customer(db: Session, customer_id: int):
    return db.query(models.Address).filter(models.Address.customer_id == customer_id).all()

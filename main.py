from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List

# Import repositories
from repositories.customer_repository import CustomerRepository
from repositories.address_repository import AddressRepository

# Import schemas
from schemas.customer import Customer, CustomerCreate
from schemas.address import Address, AddressCreate

# Import database components
from database import SessionLocal, engine
from models import Base  # Import Base after models are registered

# Create all database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ensure all models are loaded and tables are created
try:
    print("Initializing database...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")
except Exception as e:
    print(f"Error during database initialization: {e}")

# Customer Routes

@app.post("/customers/", response_model=Customer)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    customer_repo = CustomerRepository(db)
    try:
        return customer_repo.create(customer)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="A customer with this email already exists."
        )

@app.get("/customers/", response_model=List[Customer])
def get_customers(offset: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    customer_repo = CustomerRepository(db)
    return customer_repo.list(offset=offset, limit=limit)

@app.get("/customers/{customer_id}", response_model=Customer)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer_repo = CustomerRepository(db)
    customer = customer_repo.get(customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@app.put("/customers/{customer_id}", response_model=Customer)
def update_customer(customer_id: int, updated_customer: CustomerCreate, db: Session = Depends(get_db)):
    customer_repo = CustomerRepository(db)
    customer = customer_repo.get(customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer_repo.update(customer, updated_customer)

@app.delete("/customers/{customer_id}", response_model=dict)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    customer_repo = CustomerRepository(db)
    customer = customer_repo.get(customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    customer_repo.delete(customer)
    return {"detail": "Customer deleted successfully"}

# Address Routes

@app.post("/customers/{customer_id}/addresses/", response_model=Address)
def create_address(customer_id: int, address: AddressCreate, db: Session = Depends(get_db)):
    address_repo = AddressRepository(db)
    try:
        return address_repo.create(address, customer_id)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="An address with this data already exists."
        )

@app.get("/customers/{customer_id}/addresses/", response_model=List[Address])
def get_addresses_by_customer(customer_id: int, db: Session = Depends(get_db)):
    address_repo = AddressRepository(db)
    return address_repo.list_by_customer(customer_id)

@app.put("/customers/{customer_id}/addresses/{address_id}", response_model=Address)
def update_address(customer_id: int, address_id: int, updated_address: AddressCreate, db: Session = Depends(get_db)):
    address_repo = AddressRepository(db)
    address = address_repo.get(customer_id, address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    address_repo.update(address_id, updated_address)
    return address

@app.delete("/customers/{customer_id}/addresses/{address_id}", response_model=dict)
def delete_address(customer_id: int, address_id: int, db: Session = Depends(get_db)):
    address_repo = AddressRepository(db)
    address = address_repo.get(customer_id, address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    address_repo.delete(address)
    return {"detail": "Address deleted successfully"}

# Fetch all addresses
@app.get("/addresses/", response_model=List[Address])
def get_all_addresses(db: Session = Depends(get_db)):
    address_repo = AddressRepository(db)
    return address_repo.list()  # Calls the list method to fetch all addresses

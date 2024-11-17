from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Existing Endpoints

@app.post("/customers/", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db=db, customer=customer)

@app.get("/customers/", response_model=list[schemas.Customer])
def get_customers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_customers(db, skip=skip, limit=limit)

@app.get("/customers/{customer_id}", response_model=schemas.Customer)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = crud.get_customer(db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

@app.post("/customers/{customer_id}/addresses/", response_model=schemas.Address)
def create_address(customer_id: int, address: schemas.AddressCreate, db: Session = Depends(get_db)):
    return crud.create_address(db=db, address=address, customer_id=customer_id)

@app.get("/customers/{customer_id}/addresses/", response_model=list[schemas.Address])
def get_addresses_by_customer(customer_id: int, db: Session = Depends(get_db)):
    return crud.get_addresses_by_customer(db, customer_id=customer_id)

# Missing Endpoints

# PUT /customers/{customer_id} - Update a Customer
@app.put("/customers/{customer_id}", response_model=schemas.Customer)
def update_customer(customer_id: int, updated_customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = crud.get_customer(db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return crud.update_customer(db=db, db_customer=db_customer, updated_customer=updated_customer)

# DELETE /customers/{customer_id} - Delete a Customer
@app.delete("/customers/{customer_id}", response_model=dict)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = crud.get_customer(db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    crud.delete_customer(db=db, db_customer=db_customer)
    return {"detail": "Customer deleted successfully"}

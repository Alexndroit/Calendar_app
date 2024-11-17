from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# Customer model
class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    # Establish a relationship with the Address model
    addresses = relationship("Address", back_populates="owner")

# Address model
class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    street = Column(String)
    city = Column(String)
    zip_code = Column(String)
    customer_id = Column(Integer, ForeignKey("customers.id"))

    # Establish a relationship with the Customer model
    owner = relationship("Customer", back_populates="addresses")

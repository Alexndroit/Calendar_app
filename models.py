from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(length=100), nullable=False, index=True)
    email = Column(String(length=100), unique=True, nullable=False, index=True)
    age = Column(Integer, nullable=True)

    addresses = relationship("Address", back_populates="owner")

class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    street = Column(String(length=200), nullable=False)
    # Removed the street2 field
    # street2 = Column(String(length=200), nullable=True)  <-- Remove this line
    city = Column(String(length=100), nullable=False)
    zip_code = Column(String(length=5), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)

    owner = relationship("Customer", back_populates="addresses")

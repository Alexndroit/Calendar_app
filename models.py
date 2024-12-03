from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# Customer model
class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # Positive, auto-incrementing ID
    name = Column(String(length=100), nullable=False, index=True)  # Explicit length
    email = Column(String(length=100), unique=True, nullable=False, index=True)  # Explicit length
    age = Column(Integer, nullable=True)  # Optional with no restrictions at the DB level

    # Establish a relationship with the Address model
    addresses = relationship("Address", back_populates="owner")

# Address model
class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # Positive, auto-incrementing ID
    street = Column(String(length=200), nullable=False)  # Explicit length
    street2 = Column(String(length=200), nullable=True)  # Optional with explicit nullable=True
    city = Column(String(length=100), nullable=False)  # Explicit length
    zip_code = Column(String(length=5), nullable=False)  # Explicit length
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)  # Mandatory ForeignKey

    # Establish a relationship with the Customer model
    owner = relationship("Customer", back_populates="addresses")

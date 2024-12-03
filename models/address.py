from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Address(Base):
    __tablename__ = 'addresses'
    __table_args__ = {"extend_existing": True}  # Avoid table conflicts during migrations

    id = Column(Integer, primary_key=True, index=True)
    street = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    zip_code = Column(String(10), nullable=False)  # Assuming a maximum length of 10 for ZIP codes
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)

    # Relationships
    customer = relationship("Customer", back_populates="addresses")

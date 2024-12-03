from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Address(Base):
    __tablename__ = 'addresses'
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    street = Column(String(200), nullable=False)
    city = Column(String(100), nullable=False)
    zip_code = Column(Integer, nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)

    # Relationships
    customer = relationship("Customer", back_populates="addresses")

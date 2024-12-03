from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Customer(Base):
    __tablename__ = 'customers'
    __table_args__ = {"extend_existing": True}  # Add this to avoid table conflicts

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)  # Added length 255
    email = Column(String(255), unique=True, nullable=False)  # Added length 255
    age = Column(Integer, nullable=True)

    # Relationships
    addresses = relationship("Address", back_populates="customer")

from sqlalchemy import Column, String, ForeignKey, Integer  # Add Integer import
from sqlalchemy.dialects.mysql import SMALLINT  # Use mysql.SMALLINT
from sqlalchemy.orm import relationship
from models.base import Base

class Customer(Base):
    __tablename__ = 'customers'
    __table_args__ = {"extend_existing": True}  # Avoid table conflicts

    id = Column(SMALLINT(unsigned=True), primary_key=True, index=True, autoincrement=True)  # Use mysql.SMALLINT with unsigned
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    age = Column(Integer, nullable=True)

    # Relationships
    addresses = relationship("Address", back_populates="customer")

from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.dialects.mysql import SMALLINT
from sqlalchemy.orm import relationship
from models.base import Base

class Address(Base):
    __tablename__ = 'addresses'
    __table_args__ = {"extend_existing": True}

    id = Column(SMALLINT(unsigned=True), primary_key=True, index=True, autoincrement=True)
    street = Column(String(200), nullable=False)
    city = Column(String(100), nullable=False)
    zip_code = Column(SMALLINT(unsigned=True), nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)

    customer = relationship("Customer", back_populates="addresses")

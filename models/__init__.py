# Import the shared Base
from .base import Base

# Import all models here to ensure they are registered with SQLAlchemy
from .customer import Customer
from .address import Address

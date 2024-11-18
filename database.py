from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# This is the database URL
DATABASE_URL = "sqlite:///./test.db"

# This creates the database engine
engine = create_engine(DATABASE_URL)

# This creates a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# This creates a base class for our models
Base = declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging

# Enable SQLAlchemy Logging
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

# Database connection string
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:rGEkY6HnKkREfne!@mysql_db/calendar_app"

# Create the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()
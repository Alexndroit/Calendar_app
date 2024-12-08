import os
from pathlib import Path
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Print PYTHONPATH for debugging
print("PYTHONPATH:", sys.path)

# Directory root
sys.path.insert(0, r"C:\Users\Alex\Desktop\Python\Python_codes")

# Base and models
from calendar_crud_app.models.base import Base  # Correct import for Base
from calendar_crud_app import models

# This is the Alembic Config object, which provides access to the .ini file values
config = context.config

# Interpret the config file for Python logging
fileConfig(config.config_file_name)

# Set up metadata for 'autogenerate' migrations
target_metadata = Base.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

# Choose the correct migration mode
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

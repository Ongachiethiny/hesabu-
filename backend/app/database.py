from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Define where the database file will be saved.
# This creates a file named 'hesabu.db' in your project root directory.
SQLALCHEMY_DATABASE_URL = "sqlite:///./hesabu.db"

# 2. Create the engine.
# 'connect_args' is only needed for SQLite to prevent thread conflicts.
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# 3. Create a SessionLocal class.
# Each time we need to talk to the DB, we will instantiate a session from this.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Create a Base class.
# Our database tables (models) will inherit from this class.
Base = declarative_base()
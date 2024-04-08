import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData

# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from databases import Database


load_dotenv(".env")


DATABASE_URL = os.environ["DATABASE_URL"]


# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()

Base = declarative_base()


# Dependency to get the database session
def get_db_session() -> Session:  # type: ignore
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()


# Dependency to get the database connection
def get_db() -> Database:
    return Database(DATABASE_URL)  # database query builder


# Dependency to get the database connection asynchronously
async def get_async_db() -> Database:
    return Database(DATABASE_URL)  # database query builder

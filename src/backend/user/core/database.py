from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base

from .config import SQLALCHEMY_DATABASE_URL

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=10,
    max_overflow=0,
    pool_use_lifo=True,
    pool_pre_ping=True,
)
SESSION = async_sessionmaker(
    bind=engine, autocommit=False, expire_on_commit=False, autoflush=False
)

BASE = declarative_base()
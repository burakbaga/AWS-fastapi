from sqlalchemy import create_engine,engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

from core.settings import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print(SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db() ->Generator:
    try :
        db = SessionLocal()
        yield db 
    finally:
        db.close()
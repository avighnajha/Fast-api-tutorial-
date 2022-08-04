from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus as urlquote

 
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:%s@localhost/fastapi" % urlquote("Aviati@123")

engine = create_engine("postgresql://postgres:%s@localhost/fastapi" % urlquote("Aviati@123"))

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

#To add .env to gitignore, run this command:- echo ".env" >> .gitignore 

POSTGRES_DATABASE_URL = os.environ.get("POSTGRES_DATABASE_URL")

if not POSTGRES_DATABASE_URL or "POSTGRES_DATABASE_URL" in POSTGRES_DATABASE_URL:
    raise ValueError(f"ERROR: Invalid DATABASE URL -> {POSTGRES_DATABASE_URL}")

engine = create_engine(POSTGRES_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
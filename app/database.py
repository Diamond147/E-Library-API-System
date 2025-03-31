import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

POSTGRES_DATABASE_URL = os.environ.get("POSTGRES_DATABASE_URL")
#To add .env to gitignore, run this command:- echo ".env" >> .gitignore 

engine = create_engine(POSTGRES_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
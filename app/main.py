from fastapi import FastAPI
from routers.user import user_router
from routers.book import book_router
from routers.borrow import borrow_router
from routers.borrow_record import borrow_record_router
from database import engine
from model import Base

# Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(user_router, prefix="/v1/users", tags=["Users"])
app.include_router(book_router, prefix="/v1/books", tags=["Books"])
app.include_router(borrow_router, prefix="/v1/borrows", tags=["Borrows"])
# app.include_router(borrow_record_router, prefix="/v1/borrowrecord", tags=["BorrowRecords"])



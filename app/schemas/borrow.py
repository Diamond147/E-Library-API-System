from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class BorrowRecord(BaseModel):
    record_id: UUID
    user_id: UUID
    book_id: UUID
    borrow_date: datetime
    return_date: datetime


class Borrow(BaseModel): 
    return_date: datetime


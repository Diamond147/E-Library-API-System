from datetime import datetime
from uuid import UUID, uuid4
from pydantic import BaseModel


class BorrowBase(BaseModel):
    record_id: UUID = str(uuid4())
    user_id: UUID = str(uuid4())
    book_id: UUID = str(uuid4())

class Borrow(BaseModel): 
    return_date: datetime


from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field


class BorrowBase(BaseModel):
    user_id: UUID
    book_id: UUID    

class BorrowRecord(BorrowBase):
    record_id: UUID
    borrow_date: datetime = Field(default_factory=datetime.now)  # Ensures fresh timestamp
    return_date: Optional[datetime] = None

class Return(BaseModel):
    return_date: datetime


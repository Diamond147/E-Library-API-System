from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str = "first title"
    author: str = "first author"

class Book(BookCreate):
    book_id: UUID 
    is_available: bool = True 


class BookUpdate(BaseModel):
    title: Optional[str] = "Updated first title"
    author: Optional[str] = "Updated first author"

class BookPatch(BaseModel):
    title: Optional[str] = "Updated first title"
    author: Optional[str] = "Corrected first author"

# print(uuid4())
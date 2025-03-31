from typing import Optional
from uuid import UUID
from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str = "first title"
    author: str = "first author"
    is_available: bool = True

class Book(BookCreate):
    book_id: UUID 

class BookUpdate(BaseModel):
    title: Optional[str] = "Updated first title"
    author: Optional[str] = "Updated first author"
    is_available: bool = True

class BookPatch(BaseModel):
    title: Optional[str] = "Updated first title"
    author: Optional[str] = "Corrected first author"
    is_available: bool = True

# print(uuid4())
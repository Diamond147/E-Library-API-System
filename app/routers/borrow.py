from fastapi import APIRouter, status
from schemas.borrow import Borrow
from services.borrow import BorrowService

borrow_router = APIRouter()

#borrow book
@borrow_router.post("/{user_id}", status_code=status.HTTP_201_CREATED)
async def borrow_book(user_id:str, book_id:str):
    borrow = BorrowService.borrow_book(user_id, book_id)
    return {"detail": borrow, "message": "Book borrowed successfully"}


#return book
@borrow_router.patch("/return/{record_id}", status_code=status.HTTP_200_OK)
async def return_book(record_id:str, data:Borrow):
    borrow = BorrowService.return_book(record_id, data)
    return {"detail": borrow, "message": "Borrowed book returned successfully"}

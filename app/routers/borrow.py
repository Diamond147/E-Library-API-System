from fastapi import APIRouter, status, HTTPException, Depends
from schemas.borrow import BorrowBase, BorrowRecord, Return
from services.borrow import BorrowService
from sqlalchemy.orm import Session
from database import get_db

borrow_router = APIRouter()

#borrow book
@borrow_router.post("/", status_code=status.HTTP_201_CREATED)
async def borrow_book(data:BorrowBase, db:Session=Depends(get_db)):
    borrow = BorrowService.borrow_book(db, data)
    return {"detail": borrow, "message": "Book borrowed successfully"}


# #return book
# @borrow_router.patch("/return/{record_id}", status_code=status.HTTP_200_OK)
# async def return_book(record_id:str, data:Borrow):
#     borrow = BorrowService.return_book(record_id, data)
#     return {"detail": borrow, "message": "Borrowed book returned successfully"}

from fastapi import APIRouter, status
from crud.borrow_record import Borrow_Record_Crud
from db import Borrow_Records

borrow_record_router = APIRouter()

#view specific borrow record
@borrow_record_router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def view_specific_borrow_record(user_id:str):
    borrow = Borrow_Record_Crud.view_specific_borrow_record(user_id)
    return {"detail": borrow, "message": "successfully"}

# view all borrow record
@borrow_record_router.get("/", status_code=status.HTTP_200_OK)
async def view_all_borrow_record(): 
    return {"detail": Borrow_Records, "message": "successful"}
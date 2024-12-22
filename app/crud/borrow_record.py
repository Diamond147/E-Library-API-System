from fastapi import HTTPException, status
from db import Users, Books, Borrow_Records

class BorrowRecordCrud:

    @staticmethod
    def view_specific_borrow_record(user_id:str):

        if user_id not in Users:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        user_record = []
        for record_id, record_data in Borrow_Records.items():
            if record_data["user_id"] == user_id:
                user_record.append(record_data)

        if not user_record:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User has no borrow record")
        
        return user_record
    

    @staticmethod
    def view_all_borrow_record():
        return Borrow_Records

Borrow_Record_Crud = BorrowRecordCrud
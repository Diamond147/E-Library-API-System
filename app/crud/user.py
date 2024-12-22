from uuid import uuid4
from fastapi import HTTPException, status
from schemas.user import User, UserCreate, UserPatch, UserUpdate
from db import Users


class UserCrud:

    @staticmethod
    def get_users(): 
        return Users
    

    @staticmethod
    def create_user(data:UserCreate):

        for id, var in Users.items():
            if var["name"] == data.name and var["email"] == data.email:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exist")
            
        id = str(uuid4())
        new_user = User(user_id = id, **data.model_dump())
        Users[id] = new_user.model_dump()

        return new_user
    

    @staticmethod
    def get_user_by_id(user_id:str):

        if user_id not in Users:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        return Users[user_id]
    

    @staticmethod
    def update_user(user_id: str, data: UserUpdate):

        if user_id not in Users:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        Users[user_id] = data.model_dump()

        return Users[user_id]
    

    @staticmethod
    def partially_update_user(user_id: str, data:UserPatch):

        if user_id not in Users:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        Users[user_id] = data.model_dump(exclude_unset=True)

        return Users[user_id]
    

    @staticmethod
    def delete_user(user_id: str):

        if user_id not in Users:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        del Users[user_id]

        return {"message": "User deleted successfully"}
       
    
User_Crud = UserCrud()
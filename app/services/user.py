from fastapi import HTTPException, status
from db import Users


class UserService:

    @staticmethod
    def deactivate(user_id: str):
       
        if user_id not in Users:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        Users[user_id]["is_active"] = False
        
        return {
            "name": Users[user_id].get("name"),
            "email": Users[user_id].get("email"),
            "is_active": Users[user_id]["is_active"],
        } 
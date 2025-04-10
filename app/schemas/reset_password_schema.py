from pydantic import BaseModel, EmailStr
from typing import Optional

class ResetPasswordRequest(BaseModel):
    email: EmailStr
    password: str
    confirm_password: str

class ConfirmResetPassword(BaseModel):
    email: EmailStr 
    token: Optional[str] = None

class MessageResponse(BaseModel):
    message: str
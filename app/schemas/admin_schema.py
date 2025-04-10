from pydantic import BaseModel, EmailStr, validator
from typing import Optional

class Main_Admin(BaseModel):
    name : str
    email: EmailStr
    user_id : str
    role : str

class Update_Main_Admin(BaseModel):
    email: Optional[EmailStr] = None
    name: Optional[str] = None
    user_id: Optional[str] = None
    role: Optional[str] = None

    @validator('*', pre=True)
    def empty_str_to_none(cls, v):
        return v if v != '' else None


class Partner_Admin(BaseModel):
    name : str
    email: EmailStr
    user_id : str
    role : str
    password : str

class Update_Partner_Admin(BaseModel):
    email: Optional[EmailStr] = None
    name: Optional[str] = None
    user_id: Optional[str] = None
    role: Optional[str] = None
    password : Optional[str] = None

    @validator('*', pre=True)
    def empty_str_to_none(cls, v):
        return v if v != '' else None
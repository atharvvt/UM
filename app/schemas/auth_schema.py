from pydantic import BaseModel, EmailStr

class EmailRequest(BaseModel):
    email: EmailStr

class EmailOTPVerifyRequest(BaseModel):
    email: EmailStr
    otp: str

class MessageResponse(BaseModel):
    message: str

class PartnerLoginRequest(BaseModel):
    email: EmailStr
    password: str

class LoginResponse(BaseModel):
    message: str
from fastapi import APIRouter, HTTPException
from app.schemas.auth_schema import EmailRequest, EmailOTPVerifyRequest, MessageResponse
from app.utils.otp_utils import generate_otp, store_email_otp, verify_email_otp
from app.utils.email_utils import send_otp_email

router = APIRouter()

@router.post("/send-email-otp", response_model=MessageResponse)
def send_email_otp(request: EmailRequest):
    otp = generate_otp()
    store_email_otp(request.email, otp)
    if send_otp_email(request.email, otp):
        return {"message": f"OTP sent to {request.email}"}
    raise HTTPException(status_code=500, detail="Failed to send OTP email")

@router.post("/verify-email-otp", response_model=MessageResponse)
def verify_email_otp_handler(request: EmailOTPVerifyRequest):
    if verify_email_otp(request.email, request.otp):
        return {"message": "OTP Verified"}
    raise HTTPException(status_code=400, detail="Invalid or expired OTP")

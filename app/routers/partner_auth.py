from fastapi import APIRouter, HTTPException
from app.schemas.reset_password_schema import ResetPasswordRequest, ConfirmResetPassword, MessageResponse
from app.utils.reset_utils import create_reset_token 
from app.schemas.auth_schema import PartnerLoginRequest, LoginResponse
from app.utils.email_utils import send_reset_email
from app.utils.security import hash_password, verify_password
from app.sb_client import supabase

router = APIRouter()

@router.post("/partner-login", response_model=LoginResponse)
def partner_login(request: PartnerLoginRequest):
    try:
        res = supabase.table("user_partner_admin").select("*").eq("email", request.email).eq("role", "partner_admin").single().execute()
        user = res.data
        print(user)
        print(res)
        if not user:
            raise HTTPException(status_code=404, detail="Partner admin not found")

        if not verify_password(request.password, user["password"]):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        return {"message": "Login successful"}
    except Exception as e:
        print(f"Exception during login: {e}")
        raise HTTPException(status_code=500, detail="Login failed")


@router.post("/forgot-password", response_model=MessageResponse)
def forgot_password(request: ResetPasswordRequest):
    # Optional: check if user exists and is partner_admin
    res = supabase.table("user_partner_admin").select("*").eq("email", request.email).eq("role", "partner_admin").execute()
    if not res.data:
        raise HTTPException(status_code=404, detail="Partner Admin not found")

    token = create_reset_token(request.email)
    if send_reset_email(request.email, request.password, request.confirm_password):
        return {"message": "Reset email sent"}
    raise HTTPException(status_code=500, detail="Failed to send email")


@router.get("/reset-password", response_model=MessageResponse)
def reset_password(email, password, confirm_password):
    try:
        if password != confirm_password:
            raise HTTPException(status_code=400, detail="Passwords do not match")

        hashed = hash_password(password)
        supabase.table("user_partner_admin").update(
            {"password": hashed}
        ).eq("email", email).eq("role", "partner_admin").execute()

        return {"message": "Password has been reset successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update password: {e}")

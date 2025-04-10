import secrets
from datetime import datetime, timedelta
from app.sb_client import supabase

def create_reset_token(email: str) -> str:
    token = secrets.token_urlsafe(32)
    expires_at = datetime.utcnow() + timedelta(minutes=15)

    supabase.table("password_reset_tokens").upsert({
        "email": email,
        "token": token,
        "expires_at": expires_at.isoformat()
    }).execute()

    return token

# def verify_reset_token(email: str, token: str) -> bool:
#     res = supabase.table("password_reset_tokens").select("*").eq("email", email).single().execute()
#     data = res.data
#     if data and data["token"] == token and datetime.utcnow() < datetime.fromisoformat(data["expires_at"]):
#         return True
#     return False

# def delete_reset_token(email: str):
#     supabase.table("password_reset_tokens").delete().eq("email", email).execute()

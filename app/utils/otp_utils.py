import random, string
from datetime import datetime, timedelta
from app.sb_client import supabase

def generate_otp(length=6):
    return ''.join(random.choices(string.digits, k=length))

def store_email_otp(email: str, otp: str):
    expires_at = datetime.utcnow() + timedelta(minutes=5)
    supabase.table("email_otps").upsert({
        "email": email,
        "otp": otp,
        "expires_at": expires_at.isoformat()
    }).execute()

def verify_email_otp(email: str, otp: str) -> bool:
    res = supabase.table("email_otps").select("*").eq("email", email).single().execute()
    data = res.data
    if data:
        stored_otp = data['otp']
        expires_at = datetime.fromisoformat(data['expires_at'])
        if stored_otp == otp and datetime.utcnow() < expires_at:
            supabase.table("email_otps").delete().eq("email", email).execute()
            return True
    return False

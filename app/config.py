import os
from dotenv import load_dotenv
import sendlk

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
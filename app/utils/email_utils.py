import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import urllib

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
FROM_EMAIL = os.getenv("FROM_EMAIL")
FRONTEND_URL=os.getenv('FRONTEND_URL')

def send_otp_email(email: str, otp: str):
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=email,
        subject="Your OTP Code",
        html_content=f"<p>Your OTP is: <strong>{otp}</strong>. It will expire in 5 minutes.</p>"
    )
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        sg.send(message)
        return True
    except Exception as e:
        print(f"Error sending OTP email: {e}")
        return False


def send_reset_email(email: str, password : str, confirm_password : str):
    encoded_email = urllib.parse.quote(email)  # Ensure the email is safely encoded
    reset_url = f"{FRONTEND_URL}/partner-auth/reset-password?email={encoded_email}&password={password}&confirm_password={confirm_password}"
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=email,
        subject="Reset Your Partner Admin Password",
        html_content=f"<p>Click the link below to reset your password:</p><a href='{reset_url}'>{reset_url}</a><p>This link will expire in 15 minutes.</p>"
    )
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        sg.send(message)
        return True
    except Exception as e:
        print(f"Error sending reset email: {e}")
        return False
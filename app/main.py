from fastapi import FastAPI
from app.routers import auth, main_admin, partner_admin, partner_auth, refresh_token

app = FastAPI()


app.include_router(auth.router, prefix="/Main_admin_login", tags=["Main Admin Auth"])
app.include_router(main_admin.router, prefix="/main-admin", tags=["Main Admin"])
app.include_router(partner_admin.router, prefix="/partner-admin",  tags=["Partner Admin"])
app.include_router(refresh_token.router, prefix="/refresh-token", tags=["Refresh Token"])
app.include_router(partner_auth.router, prefix="/partner-auth", tags=["Partner Admin Auth"])
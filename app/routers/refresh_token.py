from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from datetime import timedelta
from app.utils.jwt import create_access_token
from app.schemas.token_schema import Token
from app.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="partner-auth/partner-login")
@router.post("/refresh-token", response_model=Token)
def refresh_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(...)
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

    # Create new token
    new_token = create_access_token(data={"sub": username}, expires_delta=timedelta(minutes=15))
    return Token(access_token=new_token, token_type="bearer")






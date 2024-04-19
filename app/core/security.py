from jose import jwt
from datetime import datetime, timedelta
from app.core import settings
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/token")

def create_token(email: str):
    token_data = {
        "sub": email,
        "exp": datetime.now() + timedelta(hours=24),
    }
    token = jwt.encode(token_data, settings.GOOGLE_CLIENT_SECRET, algorithm="HS256")
    return token

def get_email_from_token(token: str = Depends(oauth2_scheme)):
    try:
        email = jwt.decode(token, settings.GOOGLE_CLIENT_SECRET, algorithms=["HS256"]).get("sub")
        if not email:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    except jwt.JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return email
from datetime import datetime, timedelta
import os
from fastapi import (
    HTTPException,
    Request,
)
from jose import jwt, JWTError
from environs import Env

env = Env()
env.read_env(path="src/.env")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


def create_access_token(user_data: dict, expires_delta: timedelta | None = None):
    encode = user_data
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    encode.update({"exp": expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


def get_token(request: Request):
    try:
        token = request.cookies.get("access_token")
        if token is None:
            return None
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_name: str = payload.get("sub")
        user_id: int = payload.get("user_id")
        grp_id: int = payload.get("grp_id")
        role: int = payload.get("role")

        return {
            "username": user_name,
            "id": user_id,
            "grp_id": grp_id,
            "role": role,
        }
    except JWTError as error:
        raise HTTPException(status_code=404, detail=str(error))

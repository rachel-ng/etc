import os
from typing import Optional
import datetime
from datetime import timedelta

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt



SECRET_KEY = os.environ['SECRET_KEY']
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 14

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def generate_access_token(data, exp_delta: Optional[timedelta] = timedelta(minutes=15)): 
    expiration = datetime.datetime.utcnow() + exp_delta
    return jwt.encode({**data, "exp": expiration}, SECRET_KEY, algorithm=ALGORITHM)

def decode_payload(token): 
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
from typing import Generator

from sqlalchemy.orm import Session

from fastapi import Depends
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from jose import JWTError

from util.config import session_factory
from util.auth import oauth2_scheme, decode_payload
from util.models import TokenData
from util.db import get_user



def get_session() -> Generator: 
    engine, session = session_factory()

    try: 
        yield session 

    finally: 
        session.close()



async def get_current_user(session: Session = Depends(get_session), 
                           token: str = Depends(oauth2_scheme)):
  
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_payload(token)
        username = payload.get("sub")

        if username is None:
            raise credentials_exception

        token_data = TokenData(username=username)

    except JWTError:
        raise credentials_exception

    user = get_user(session, token_data.username)

    if user is None:
        raise credentials_exception

    return user

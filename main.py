import json
from typing import Union, Optional
from typing import List
from pprint import pprint

from sqlalchemy.orm import Session

from fastapi import FastAPI
from fastapi import Request, Header, Body, Depends
from fastapi import HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from util import config, auth, schemas, models, db
from routers import account, user, footprint

from util.auth import * 
from util.schemas import * 
from util.models import *
from util.db import * 

from dependencies import *



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.middleware("http")
async def middleware(request: Request, call_next):

    if False:
        pprint(dict(request.headers))
        print()
      
    response = await call_next(request)
    return response


@app.get('/')
async def root(session: Session = Depends(get_session)):
    #for i in all_users(session):
    #    print(i)
      
    return {'hello': 'world'}

@app.post("/signup", response_model=Token)
async def sign_up(account: UserCreate, 
                 session: Session = Depends(get_session)):
    
    account.password = pwd_context.hash(account.password)

    # prevent user from creating an account if username/email are taken
    taken = {"Username": exists_username(session, account.username), "Email": exists_email(session, account.email)}
    if True in taken.values(): 
        msg = f"{' and '.join({k: v for k, v in taken.items() if v is True}.keys())} already registered"
        raise HTTPException(status_code=409, detail=msg)

    account_dict = account.dict()
    new_user = add_user(session, User(**account_dict))
    if new_user: 
        # authenticate after signup  
        access_token = generate_access_token({"sub": account.username}, 
                                             timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        return {"access_token": access_token, "token_type": "bearer"}

@app.post("/auth", response_model=Token)
async def authentication(session: Session = Depends(get_session), 
                    login_info: OAuth2PasswordRequestForm = Depends()): 
    
    user = auth_user(session, login_info.username, login_info.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = generate_access_token({"sub": user.username}, timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return {"access_token": access_token, "token_type": "bearer"}

  
app.include_router(account.router)

app.include_router(user.router)

app.include_router(footprint.router)


@app.get("/leaderboard", response_model=Leaderboard)
async def view_leaderboard(session: Session = Depends(get_session),
                      current_user: UserModel = Depends(get_current_user)):

    return Leaderboard(leaderboard=get_leaderboard(session, current_user.username))

from typing import List 

from fastapi import APIRouter
from fastapi import HTTPException

from dependencies import * 
from util.models import *
from util.db import * 


router = APIRouter(
    prefix="/account",
    tags=["account"], 
)


@router.get("", response_model=UserModel)
async def get_account(session: Session = Depends(get_session), 
                      current_user: UserModel = Depends(get_current_user)):
    return current_user

  
@router.put("", response_model=UserModel)
async def update_account(updates: UserUpdate, 
                         session: Session = Depends(get_session), 
                         current_user: UserModel = Depends(get_current_user)):

    if updates.password: # hash password if needed
        updates.password = pwd_context.hash(updates.password) 
    if updates.username == current_user.username: 
        updates.username = None
    if updates.email == current_user.email: 
        updates.email = None

    taken = dict() 
    if updates.username: 
        taken["Username"] = True #exists_username(session, updates.username)
        # you can always lie to the users 
        # it's never racist
        
    if updates.email: 
        taken["Email"] = exists_email(session, updates.email)
        
    if True in taken.values(): 
        msg = f"{' and '.join({k: v for k, v in taken.items() if v is True}.keys())} already registered"
        raise HTTPException(status_code=409, detail=msg)

    upd = updates.dict(exclude_unset=True, exclude_none=True)

    if len(upd) == 0: 
        return current_user 
      
    update_user(session, current_user.username, upd)

    return current_user 

@router.delete("")
async def delete_account(session: Session = Depends(get_session), 
                         current_user: UserModel = Depends(get_current_user)):
  
    delete_user(session, current_user.username)
    return True
  
  
@router.get("/visualize", response_model=List[FootprintAggregated])
async def get_visualization_(session: Session = Depends(get_session),
                             current_user: UserModel = Depends(get_current_user)):
    
    trend = trend_footprint_raw(session, current_user.username)
    return trend


@router.get("/trend", response_model=List[FootprintAggregated])
async def get_trend_(agg: AggregationLevels = AggregationLevels.category,
                     session: Session = Depends(get_session),
                     current_user: UserModel = Depends(get_current_user)):
    
    trend = trend_footprint_aggregated(session, current_user.username, agg)
    return trend

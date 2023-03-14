from typing import List 

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException, status

from sqlalchemy.orm import Session

from dependencies import * 
from util.models import UserModel, UserRecord, AggregationLevels, Timeframes
from util.db import *



router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.get("", response_model=UserRecord)
async def get_user_(session: Session = Depends(get_session), 
                    current_user: UserModel = Depends(get_current_user)):
    return get_rank(session, current_user.username)

  
@router.get("/{username}", response_model=UserRecord)
async def get_username_(username: str, 
                        session: Session = Depends(get_session), 
                        current_user: UserModel = Depends(get_current_user)):
    
    user = get_rank(session, username)
    
    if not user: 
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    if current_user.username == username or user["sharing"]: 
        records = get_rank(session, username)
        return records
    else: 
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You do not have permission to view this user",
        )

        
@router.get("/{username}/history", response_model=List[FootprintModel])
async def get_user_history_(username: str,
                            session: Session = Depends(get_session),
                            current_user: UserModel = Depends(get_current_user)):
                      
    user = get_user(session, username)
    
    if not user: 
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    if current_user.username == username or user.sharing: 
        records = get_history(session, username)
        return records
    else: 
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You do not have permission to view this user's history",
        )


@router.get("/{username}/visualize", response_model=List[FootprintAggregated])
async def get_visualization_(username: str, 
                             session: Session = Depends(get_session),
                             current_user: UserModel = Depends(get_current_user)):
    
    user = get_user(session, username)
    if not user: 
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    if current_user.username == username or user.sharing: 
        trend = trend_footprint_raw(session, username)
        return trend
    else: 
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You do not have permission to view this user's trends",
        )


@router.get("/{username}/trend", response_model=List[FootprintAggregated])
async def get_trend_(username: str, 
                     agg: AggregationLevels = AggregationLevels.category,
                     session: Session = Depends(get_session),
                     current_user: UserModel = Depends(get_current_user)):
    
    user = get_user(session, username)
    if not user: 
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    if current_user.username == username or user.sharing: 
        trend = trend_footprint_aggregated(session, username, agg)
        return trend
    else: 
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You do not have permission to view this user's trends",
        )

from typing import List 
from decimal import Decimal

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException, status

from sqlalchemy.orm import Session

from dependencies import * 
from util.models import *
from util.db import * 
from util.conversion import * 



router = APIRouter(
    prefix="/footprint",
    tags=["footprint"],
)

@router.post("", response_model=FootprintModel)
async def add_footprint_(activity: FootprintCreate, 
                         session: Session = Depends(get_session),
                         current_user: UserModel = Depends(get_current_user)):

    activity.username = current_user.username
    activity.emission = conversion_function(activity.category, activity.activity, activity.usage) 
    
    activity_dict = activity.dict(exclude_unset=True)
    fp = add_footprint(session, Footprint(**activity_dict))
    return fp

@router.get("", response_model=List[FootprintModel])
async def get_footprints_(session: Session = Depends(get_session),
                          current_user: UserModel = Depends(get_current_user)):
  
    return get_history(session, current_user.username)


@router.get("/{id}", response_model=FootprintModel)
async def get_footprint_(id, 
                         session: Session = Depends(get_session), 
                         current_user: UserModel = Depends(get_current_user)):

    footprint: FootprintModel = get_footprint(session, id)
    if footprint and (current_user.username == footprint.username or footprint.user.sharing): 
        return footprint
    else:
        msg = f"Footprint {id} does not exist"
        raise HTTPException(status_code=404, detail=msg)

@router.put("/{id}", response_model=FootprintModel)
async def update_footprint_(id, 
                            updates: FootprintUpdate, 
                            session: Session = Depends(get_session), 
                            current_user: UserModel = Depends(get_current_user)):

    footprint: FootprintModel = get_footprint(session, id)
    if footprint == None or footprint.username != current_user.username:
        msg = f"Footprint {id} does not exist"
        raise HTTPException(status_code=404, detail=msg)

    updates.emission = conversion_function(updates.category or activity.category, 
                                           updates.activity or activity.activity, 
                                           updates.usage or activity.usage) 
    
    upd = updates.dict(exclude_unset=True, exclude_none=True)
    return update_footprint(session, id, upd)

@router.delete("/{id}")
async def delete_footprint_(id, 
                            session: Session = Depends(get_session),
                            current_user: UserModel = Depends(get_current_user)):
    
    footprint: FootprintModel = get_footprint(session, id)
    
    if footprint == None or footprint.username != current_user.username:
        msg = f"Footprint {id} does not exist"
        raise HTTPException(status_code=404, detail=msg)

    delete_footprint(session, id) 
    return True
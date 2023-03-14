from pydantic import BaseModel
from enum import Enum
from typing import Union, Optional
from typing import List
from decimal import Decimal 
import datetime



class UserBase(BaseModel): 
    username: str
    email: str 
    sharing: bool = True

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase): 
    username: Optional[str]
    email: Optional[str]
    sharing: Optional[bool]
    password: Optional[str]

class FootprintBase(BaseModel):
    username: Optional[str]
    timestamp: Union[datetime.datetime, datetime.date]
    category: str
    activity: str

    usage: Decimal
    emission: Optional[Decimal]

    class Config:
        orm_mode = True

class FootprintCreate(FootprintBase):
    pass

  
class UserModel(UserBase):
    pass


class FootprintModel(FootprintCreate):
    id: Optional[int]
    user: Optional[UserBase]

class FootprintUpdate(BaseModel):
    timestamp: Optional[Union[datetime.datetime, datetime.date]]
    usage: Optional[Decimal]
    emission: Optional[Decimal]
    category: Optional[str]
    activity: Optional[str]

class FootprintAggregated(FootprintBase):
    usage: Optional[Decimal]
    category: Optional[str]
    activity: Optional[str]

class FootprintsList(BaseModel): 
    records: List[FootprintModel]


class UserRecord(BaseModel): 
    rank: int
    user: str
    sharing: bool
    footprint: Optional[Decimal]
    
class Leaderboard(BaseModel): 
    leaderboard: List[UserRecord]


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str]


class AggregationLevels(str, Enum):
    date = "date"
    category = "category"
    activity = "activity"

class Timeframes(str, Enum):
    week = "week"
    w = "w"
    month = "month"
    m = "m"

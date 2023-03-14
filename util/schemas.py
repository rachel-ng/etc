from sqlalchemy import Column, String, Integer, Numeric,  Boolean, DateTime, Date, ForeignKey, Table
from sqlalchemy.orm import relationship, backref

from util.config import Base



class User(Base):
    __tablename__ = "user"
    username = Column(String, primary_key=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    sharing = Column(Boolean, default=True) 

    history = relationship("Footprint", 
                            back_populates = "user",
                            passive_deletes=True
                            )
    
    __repr_blacklist__ = ['password']

class Footprint(Base):
    __tablename__ = "footprint"
    id = Column(Integer, primary_key=True)
    username = Column(String, 
                      ForeignKey("user.username", ondelete="CASCADE", onupdate="CASCADE"), nullable=False) 
    timestamp = Column(DateTime, nullable=False)  
    category = Column(String)  
    activity = Column(String) 
    usage = Column(Numeric, nullable=False) 
    
    emission = Column(Numeric, nullable=False) 

    user = relationship("User", back_populates = "history")

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.engine import Engine
from sqlalchemy import event

from sqlalchemy_repr import RepresentableBase, PrettyRepresentableBase
Base = declarative_base(cls=RepresentableBase)



DB_FILE = '.data/data.db'  # db file


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON") # allow for foreign key usage with sqlite
    cursor.close()

def session_factory(DB_FILE=DB_FILE): 
    DB_URL = "sqlite:///{}".format(DB_FILE)
    #print(DB_FILE, "\t", DB_URL)
    
    engine = create_engine(DB_URL,
                           connect_args={"check_same_thread": False}
    )
    Base.metadata.create_all(engine)
    _SessionFactory = sessionmaker(bind=engine)
    return engine, _SessionFactory()

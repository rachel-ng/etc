import datetime 
from datetime import timedelta

from sqlalchemy.orm import Session
from sqlalchemy import func, cast, and_, or_, not_
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from util.schemas import * 
from util.models import FootprintModel, FootprintAggregated
from util.auth import pwd_context



def all_users(session): 
    return session.query(User).all() 

def add_user(session, entry: User):
    try:
        existing_entry = session.query(User).filter(
                or_(User.username == entry.username,
                    User.email == entry.email))\
            .one_or_none()
        if existing_entry == None:
            session.add(entry)
            session.commit()
            session.refresh(entry)
            return entry
        else:
            print("User exists in database: {}".format(existing_entry))
            return False
    except IntegrityError as e:
        print(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        print("ERROR when adding User: {}".format(e))
        raise e

def get_user(session, username):
    return session.query(User).get(username)

def update_user(session, username, updates: dict):
    session.query(User).filter(User.username == username).update(updates)
    session.commit()

def delete_user(session: Session, username):
    session.query(User).filter(User.username == username).delete()
    session.commit()


def auth_user(session, username, password):
    user = get_user(session, username)

    if not user: 
        return False

    if not pwd_context.verify(password, user.password):
        return False 
    
    return user


def get_user_name(session, username):
    return session.query(User).filter(User.username == username).one_or_none()

def exists_username(session, username):
    return session.query(User).filter(User.username == username).one_or_none() != None

def get_user_email(session, email):
    return session.query(User).filter(User.email == email).one_or_none()

def exists_email(session, email):
    return session.query(User).filter(User.email == email).one_or_none() != None
  
  
def get_history(session, username): 
    return get_user(session, username).history


def get_user_footprint(session, username): 
    return sum(i.emission for i in get_history(session, username))


  
def all_footprints(session): 
    return session.query(Footprint).all()

def add_footprint(session, entry: Footprint):
    try:
        session.add(entry)
        session.commit()
        session.refresh(entry)
        return entry 
    except IntegrityError as e:
        print(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        print("ERROR when adding Footprint: {}".format(e))
        raise e

def get_footprint(session, id): 
    return session.query(Footprint).get(id)

def update_footprint(session, id, updates: dict):
    session.query(Footprint).filter(Footprint.id == id).update(updates)
    session.commit()
    return session.query(Footprint).filter(Footprint.id == id).one_or_none()

def delete_footprint(session, id):
    session.query(Footprint).filter(Footprint.id == id).delete()
    session.commit()

  
  
def get_leaderboard_raw(session, n=-1):
    q = session.query(Footprint.username, User.sharing, func.sum(Footprint.emission).label("footprint"))
    q = q.join(User)\
         .group_by(Footprint.username)\
         .order_by(func.sum(Footprint.emission).asc())

    return q.all() if n < 0 else q.limit(n).all()

def get_leaderboard_dict(session, n=-1): 
    d = {u[0]: {"user": u[0], 
                "sharing": u[1], 
                "footprint": u[2], 
                "rank": i+1
               } 
         for i,u in enumerate(get_leaderboard_raw(session, n))
        }
    return d

def get_leaderboard_anon(session, username=None, n=-1):
    leaderboard = get_leaderboard_dict(session, n)

    board = dict() 
    for i in leaderboard: 
        if not leaderboard[i]["sharing"]: 
          leaderboard[i]["user"] = leaderboard[i]["user"] if leaderboard[i]["user"] == username else f"Taylor Swift {leaderboard[i]['rank']}"
        board[leaderboard[i]['rank']] = leaderboard[i]

    return board 

def get_leaderboard(session, username, n=-1): 
    anon_leaderboard = get_leaderboard_anon(session, username, n)

    leaderboard = []
    for i in range(len(anon_leaderboard)):
        leaderboard.append(anon_leaderboard[i+1])

    return leaderboard


def get_rank(session, username): 
    return get_leaderboard_dict(session).get(username)

  
  
def trend_footprint_raw(session, username, f="week", date=datetime.datetime.utcnow().date()):
    year = date.year 
    month = date.month
    week = date.isocalendar()[1]

    tf = {
        "week": ('%W', str(week)), # week number of year
        "w": ('%W', str(week)), 

        "month": ('%m', str(month)), 
        "m": ('%m', str(month)), 
    }

    q = session.query(Footprint)
    q = q.filter(Footprint.username == username, 
                 func.strftime('%Y',(Footprint.timestamp)) == str(year),\
                 func.strftime(tf[f][0],(Footprint.timestamp)) == tf[f][1])\
         .order_by(Footprint.timestamp.asc())\

    return [FootprintModel.from_orm(f) for f in q]

def trend_footprint_aggregated(session, username, agg="category", f="week", date=datetime.datetime.utcnow().date()):
    year = date.year 
    month = date.month
    week = date.isocalendar()[1]

    levels = {
        "date": (Footprint.username, func.date(Footprint.timestamp).label("timestamp")), 
        "category": (Footprint.username, func.date(Footprint.timestamp).label("timestamp"), Footprint.category), 
        "activity": (Footprint.username, func.date(Footprint.timestamp).label("timestamp"), Footprint.category, Footprint.activity), 
    }
    
    tf = {
        "week": ('%W', str(week)), # week number of year
        "w": ('%W', str(week)), 

        "month": ('%m', str(month)), 
        "m": ('%m', str(month)), 
    }

    q = session.query(*levels[agg], func.sum(Footprint.emission).label("emission"))
    q = q.filter(Footprint.username == username, 
                 func.strftime('%Y',(Footprint.timestamp)) == str(year),
                 func.strftime(tf[f][0],(Footprint.timestamp)) == tf[f][1]
          )\
         .group_by(*levels[agg])\
         .order_by(Footprint.timestamp.asc())

    return [FootprintAggregated.from_orm(f) for f in q]

#!/usr/bin/python3
"""This script is used to query all state objects from database"""


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).order_by(State.id).first()
    if query:
        print("{}: {}".format(query.id, query.name))
    else:
        print("Nothing")

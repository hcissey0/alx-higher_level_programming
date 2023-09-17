#!/usr/bin/python3
"""This script deletes a state that has letter a in it"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    to_delete = session.query(State).filter(State.name.ilike("%a%")).all()
    for i in to_delete:
        session.delete(i)
    session.commit()

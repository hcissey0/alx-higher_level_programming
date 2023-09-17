#!/usr/bin/python3
"""This script filters the state containing an a"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for query in session.query(State).order_by(State.id).\
            filter(State.name.ilike("%a%")):
        print("{}: {}".format(query.id, query.name))

#!/usr/bin/python3
"""This script is used to list all city objects"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import State
from relationship_city import City
import sys


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id).all():
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
    session.close()

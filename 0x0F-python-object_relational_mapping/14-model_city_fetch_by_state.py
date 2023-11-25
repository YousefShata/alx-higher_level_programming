#!/usr/bin/python3
"""
fetch all
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


def main():
    """
    main Doc
    """

    user = argv[1]
    password = argv[2]
    db = argv[3]
    engine = create_engine(
               'mysql+mysqldb://{}:{}@localhost/{}'
               .format(user,
                       password,
                       db),
               pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    rows = session.query(State, City).join(City).order_by(City.id).all()
    for state, city in rows:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    session.close()


if __name__ == "__main__":
    main()

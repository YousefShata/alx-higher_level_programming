#!/usr/bin/python3
"""
fetch all
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


def main():
    """
    main Doc
    """

    user = argv[1]
    password = argv[2]
    db = argv[3]
    search = argv[4]
    engine = create_engine(
               'mysql+mysqldb://{}:{}@localhost/{}'
               .format(user,
                       password,
                       db),
               pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    state = session.query(State).filter(State.name == search).first()
    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()


if __name__ == "__main__":
    main()

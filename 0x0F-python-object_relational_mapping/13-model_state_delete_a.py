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
    engine = create_engine(
               'mysql+mysqldb://{}:{}@localhost/{}'
               .format(user,
                       password,
                       db),
               pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    states = session.query(State).filter(State.name.contains('a')).all()
    for state in states:
        session.delete(state)
    session.commit()
    session.close()


if __name__ == "__main__":
    main()

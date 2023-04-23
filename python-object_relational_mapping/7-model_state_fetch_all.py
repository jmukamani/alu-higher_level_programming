#!/usr/bin/python3
# script that lists all State objects from the database hbtn_0e_6_usa
"""import sys and MySQLdb"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                            pool-pre_ping=True)
    session = sessionmaker(bind=engine)
    session = session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

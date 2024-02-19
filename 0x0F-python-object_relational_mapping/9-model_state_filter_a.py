#!/usr/bin/python3

"""
Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa
Usage:-
    ./9-model_state_filter_a.py <mysql username>,
    <mysql password> <database name>
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).order_by(State.id)\
            .filter(State.name.like('%a%')):
        print(f'{instance.id}: {instance.name}')

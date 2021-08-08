#!/usr/bin/python3
"""
script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""

if (__name__ == "__main__"):
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from model_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for state, city in session.query(State, City).\
filter(State.id == City.state_id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()

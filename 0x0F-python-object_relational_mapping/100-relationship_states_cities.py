#!/usr/bin/python3
"""
State class:
In addition to previous requirements, the class attribute
cities must represent a relationship with the class City.
If the State object is deleted, all linked City objects
must be automatically deleted. Also, the reference from a
City object to his State should be named state
You must use the module SQLAlchemy
Script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa: (100-relationship_states_cities.py)
"""

if (__name__ == "__main__"):
    from sys import argv
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
    session.close()

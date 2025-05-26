#!/usr/bin/env python3

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models import Company, Dev, Freebie

# create engine and session

engine=create_engine("sqlite:///freebies.db")
Session=sessionmaker(bind=engine)
session=Session()

def seed_data():
    # create some companies# create engine and session

engine=create_engine("sqlite:///freebies.db")
Session=sessionmaker(bind=engine)
session=Session()

def seed_data():
    # create some companies
    c1=Company(name='Jedaq', founding_year=2005)
    c2=Company(name='Amazon', founding_year=2010)

    # now let me create some devs here
    d1=Dev(name="Alice")
    d2=Dev(name="Aquila")

    # Add companies and devs to session
    session.add_all([c1,c2,d1,d2])
    session.commit() #commit to generate ids for foreign keys

    # create freebies liked w


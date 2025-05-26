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

    


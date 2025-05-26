#!/usr/bin/env python3

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


# set up DB session

engine=create_engine("sqlite:///freebies.db")
Session =sessionmaker(bind=engine)
session=Session()







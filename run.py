#!/usr/bin/env python3

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from lib.models import Dev, Company, Freebie


# set up DB session

engine=create_engine("sqlite:///freebies.db")
Session =sessionmaker(bind=engine)
session=Session()


def print_line():
    print("_"*60)

def list_devs():
    devs=session.query(Dev).all()
    print_line()
    for dev in devs:
        print(f"{dev.id}: {dev.name}")
    print_line()







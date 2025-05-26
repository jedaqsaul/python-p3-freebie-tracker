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

    #create freebies linked to companies and devs

    f1 =Freebie(item_name='Sticker Pack', value=0, company_id=c1.id, dev_id=d1.id)
    f2 =Freebie(item_name='T-shirt', value=20, company_id=c2.id, dev_id=d2.id)
    f3 =Freebie(item_name='Mug', value=10, company_id=c1.id, dev_id=d2.id)

    # add freebies and commit
    session.add_all([f1,f2,f3])
    session.commit()

    print("Seed data added successfully!")

if __name__ =="__main__":
    seed_data()

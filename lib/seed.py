#!/usr/bin/env python3

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models import Company, Dev, Freebie


engine = create_engine("sqlite:///freebies.db", echo=False)


Session = sessionmaker(bind=engine)
session = Session()

def seed_data():
    
    c1 = Company(name="TechCorp", founding_year=2005)
    c2 = Company(name="DevSolutions", founding_year=2010)

    
    d1 = Dev(name="Alice")
    d2 = Dev(name="Bob")

   
    session.add_all([c1, c2, d1, d2])
    session.commit()  

    
    f1 = Freebie(item_name="Sticker Pack", value=0, company_id=c1.id, dev_id=d1.id)
    f2 = Freebie(item_name="T-Shirt", value=20, company_id=c2.id, dev_id=d2.id)
    f3 = Freebie(item_name="Mug", value=10, company_id=c1.id, dev_id=d2.id)

  
    session.add_all([f1, f2, f3])
    session.commit()

    print("Seed data added successfully! 🌱")





if __name__ == "__main__":
    seed_data()

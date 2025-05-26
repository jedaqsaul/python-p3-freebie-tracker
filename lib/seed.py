#!/usr/bin/env python3

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models import Company, Dev, Freebie, Base

# Create engine and session
engine = create_engine("sqlite:///freebies.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def seed_data():
    # Create some companies
    c1 = Company(name="TechCorp", founding_year=2005)
    c2 = Company(name="DevSolutions", founding_year=2010)

    # Create some devs
    d1 = Dev(name="Alice")
    d2 = Dev(name="Bob")

    # Add companies and devs to session
    session.add_all([c1, c2, d1, d2])
    session.commit()  # Commit to generate ids for FKs

    # Create freebies linked to companies and devs
    f1 = Freebie(item_name="Sticker Pack", value=0, company_id=c1.id, dev_id=d1.id)
    f2 = Freebie(item_name="T-Shirt", value=20, company_id=c2.id, dev_id=d2.id)
    f3 = Freebie(item_name="Mug", value=10, company_id=c1.id, dev_id=d2.id)

    # Add freebies and commit
    session.add_all([f1, f2, f3])
    session.commit()

    print("Seed data added successfully!")

if __name__ == "__main__":
    seed_data()

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

def list_companies():
    companies=session.query(Company).all()
    print_line()
    for company in companies:
        print(f"{company.id} : {company.name} (Founded {company.founding_year})")
    print_line()

    

def list_freebies():
    freebies = session.query(Freebie).all()
    print_line()
    for freebie in freebies:
        print(f"{freebie.item_name} (worth ${freebie.value})")
        print(f" - Given by: {freebie.company.name}")
        print(f" - Received by: {freebie.dev.name}")
        print_line()



def main():
    while True:
        print("\nFREEBIE TRACKER CLI")
        print("1. List all developers")
        print("2. List all companies")
        print("3. List all freebies")

        print("0. Exit")
        
        choice=input("Select and option: ")

        if choice == "1":
            list_devs()
        elif choice == "2":
            list_companies()
        elif choice == "3":
            list_freebies()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
        





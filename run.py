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

def show_developer_freebies():
    name = input("Enter the developer's name: ")

    dev = session.query(Dev).filter(Dev.name == name).first()

    if not dev:
        print(f"No developer found with the name {name}")
        return

    if not dev.freebies:
        print(f"{dev.name} has not received any freebies yet.")
        return

    print(f"Freebies for {dev.name}:")
    for freebie in dev.freebies:
        print(f"- {freebie.item_name} from {freebie.company.name} (Worth: ${freebie.value})")
    
       



def main():
    cli_actions = {
    "1": list_devs,
    "2": list_companies,
    "3": list_freebies,
    "4": show_developer_freebies, 
}

    while True:
        print("\nFREEBIE TRACKER CLI")
        print("1. List all developers")
        print("2. List all companies")
        print("3. List all freebies")
        print("4. Show all freebies for a developer")
        print("0. Exit")
        
        choice=input("Select and option: ")

        if choice == "0":
            print("Goodbye!")
            break
        action=cli_actions.get(choice)

        if action:
            action()
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
        





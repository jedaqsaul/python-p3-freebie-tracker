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
    # list all devs here

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

    # list all freebies

def list_freebies():
    freebies = session.query(Freebie).all()
    print_line()
    for freebie in freebies:
        print(f"{freebie.item_name} (worth ${freebie.value})")
        print(f" - Given by: {freebie.company.name}")
        print(f" - Received by: {freebie.dev.name}")
        print_line()
    
    # show freebies for a developer

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

        # add a new dev
def add_dev():
    name = input("Enter the developer's name: ")

    if not name.strip():
        print("Name cannot be empty.")
        return

    try:
        dev = Dev(name=name)
        session.add(dev)
        session.commit()
        printMessage("Developer added successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
        session.rollback()

def add_company():
    name = input("Enter company name: ")
    founding_year = input("Enter founding year: ")

    if not founding_year.isdigit():
        printMessage("Founding year must be a number.")
        return

    try:
        company = Company(
            name=name,
            founding_year=int(founding_year)
        )
        session.add(company)
        session.commit()
        printMessage("Company added successfully!")
    except Exception as e:
        printMessage(f"Error occurred: {e}")
        session.rollback()

        # add a new freebie
def add_freebie():
    try:
        print("\n--- Add a New Freebie ---")

        item_name = input("Enter the freebie item name: ")
        
        while True:
            value = input("Enter the value of the freebie: ")
            if value.isdigit():
                value = int(value)
                break
            else:
                print("Value must be a number. Try again.")

        dev_id = input("Enter the ID of the developer receiving the freebie: ")
        company_id = input("Enter the ID of the company giving the freebie: ")

        if not (dev_id.isdigit() and company_id.isdigit()):
            print("Developer ID and Company ID must be numbers.")
            return

        freebie = Freebie(
            item_name=item_name,
            value=value,
            dev_id=int(dev_id),
            company_id=int(company_id),
        )

        session.add(freebie)
        session.commit()
        printMessage(" Freebie added successfully!")

    except Exception as e:
        print(f" An error occurred: {e}")
        session.rollback()

# delete a dev here
def delete_dev():
    try:
        dev_id = input("Enter the ID of the developer to delete: ")
        if not dev_id.isdigit():
            print(" ID must be a number.")
            return

        dev = session.query(Dev).get(int(dev_id))
        if not dev:
            print(" Developer not found.")
            return

        session.delete(dev)
        session.commit()
        printMessage(f" Developer '{dev.name}' deleted successfully!")

    except Exception as e:
        print(f" Error: {e}")
        session.rollback()
# delete a company function
def delete_company():
    try:
        company_id = input("Enter the ID of the company to delete: ")
        if not company_id.isdigit():
            print("ID must be a number.")
            return

        company = session.query(Company).get(int(company_id))
        if not company:
            print("Company not found.")
            return

        session.delete(company)
        session.commit()
        printMessage(f" Company '{company.name}' deleted successfully!")

    except Exception as e:
        print(f" Error: {e}")
        session.rollback()

# delete a freebie function here
def delete_freebie():
    try:
        freebie_id = input("Enter the ID of the freebie to delete: ")
        if not freebie_id.isdigit():
            print(" ID must be a number.")
            return

        freebie = session.query(Freebie).get(int(freebie_id))
        if not freebie:
            print(" Freebie not found.")
            return

        session.delete(freebie)
        session.commit()
        printMessage(f" Freebie '{freebie.item_name}' deleted successfully!")

    except Exception as e:
        print(f"Error: {e}")
        session.rollback()

# update a dev here : 
def update_dev():
    while True:
        dev_id = input("Enter the developer ID: ")
        if not dev_id.isdigit():
            print("Developer ID must be a number. Try again!")
            continue

        try:
            dev = session.query(Dev).filter_by(id=dev_id).one_or_none()
            if dev:
                name = input("Enter the updated name: ")

                dev.name = name or dev.name
                session.commit()
                printMessage("Developer updated successfully!")
                return
            else:
                printMessage("Invalid Developer ID. Try again!")
        except Exception as e:
            print(f"Error occurred: {e}")
            session.rollback()
# update company here:

def update_company():
    while True:
        company_id = input("Enter the company ID: ")
        if not company_id.isdigit():
            print("Company ID must be a number. Try again!")
            continue

        try:
            company = session.query(Company).filter_by(id=company_id).one_or_none()
            if company:
                name = input("Enter the updated company name: ")
                year = input("Enter the updated founding year: ")

                company.name = name or company.name
                company.founding_year = int(year) if year.isdigit() else company.founding_year

                session.commit()
                printMessage("Company updated successfully!")
                return
            else:
                printMessage("Invalid Company ID. Try again!")
        except Exception as e:
            print(f"Error occurred: {e}")
            session.rollback()

# update freebie here 

def update_freebie():
    while True:
        freebie_id = input("Enter the freebie ID: ")
        if not freebie_id.isdigit():
            print("Freebie ID must be a number. Try again!")
            continue

        try:
            freebie = session.query(Freebie).filter_by(id=freebie_id).one_or_none()
            if freebie:
                name = input("Enter the updated item name: ")
                value = input("Enter the updated value: ")

                freebie.item_name = name or freebie.item_name
                freebie.value = int(value) if value.isdigit() else freebie.value

                session.commit()
                printMessage("Freebie updated successfully!")
                return
            else:
                printMessage("Invalid Freebie ID. Try again!")
        except Exception as e:
            print(f"Error occurred: {e}")
            session.rollback()








    
       

def printMessage(message):
    print(
        f"\n-----------------------------------------------\n{message}\n------------------------------------------------"
    )


def main():
    cli_actions = {
    "1": list_devs,
    "2": list_companies,
    "3": list_freebies,
    "4": show_developer_freebies, 
    "5": add_dev, 
    "6": add_company,
    "7": add_freebie,
    "8": delete_dev,
    "9": delete_company,
    "10": delete_freebie,
    "11": update_dev,
    "12": update_company,
    "13": update_freebie,



}

    while True:
        print("\nFREEBIE TRACKER CLI")
        print("1. List all developers")
        print("2. List all companies")
        print("3. List all freebies")
        print("4. Show all freebies for a developer")
        print("5. Add a new developer")
        print("6. Add a new company")
        print("7. Add a new freebie")
        print("8. Delete a developer")
        print("9. Delete a Company")
        print("10. Delete a Freebie")
        print("11. Update a developer")
        print("12. Update a company")
        print("13. Update a freebie")
        print("0. Exit")
        
        choice=input("Select and option: ")

        if choice == "0":
            print(
                "-----------------------------------------------\nThank you for visiting us. Welcome again!\n------------------------------------------------"
            )
            break
        action=cli_actions.get(choice)

        if action:
            action()
        else:
            print("Invalid option. Try again.")
            print("*************************************************************")

if __name__ == "__main__":
    main()
        





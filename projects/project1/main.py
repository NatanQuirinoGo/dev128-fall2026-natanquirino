# Starting file for Project 1
# Be sure to include your name, date, and DEV 128 in the comments header
# Natan Quirino Gonzalez
# 11/7/2026
# DEV 128


# Reconstructed from "Beginning Python - Working with SQLite - Part 1"
# This represents the expanded version shown near the end of the video.

# import the sqlite3 database module
import sqlite3
import string
print("SQLite Practice - Example User Table\n")



# create a connection to the database file
conn = sqlite3.connect("myDatabase.db")

# create a cursor that we will use to move through the database
cursor = conn.cursor()

# check if the user table already exists, if so, drop it so we can start with a new table
cursor.execute("DROP TABLE IF EXISTS user;")

# create the table if it doesn't already exist
# note that primary keys are automatically created in sqlite3 and referenced as rowid
cursor.execute("CREATE TABLE user (first_name TEXT, last_name TEXT, email TEXT, phone TEXT, street_address TEXT, city TEXT, state TEXT, zip_code TEXT)")

cursor.execute("SELECT COUNT(*) FROM user")
if cursor.fetchone()[0] == 0:
    starter_agents = [
        ("Jake", "Fromstatefarm", "jake@goodneighbor.com", "555-321-0001", "100 Khakis Lane", "Bloomington", "IL", "61701"),
        ("Linda", "Goodneighbor", "linda@goodneighbor.com", "555-321-0002", "42 Policy Ave", "Renton", "WA", "98057"),
        ("Marcus", "Coverage", "marcus@goodneighbor.com", "555-321-0003", "7 Premium Blvd", "Dallas", "TX", "75201"),
        ("Priya", "Deductible", "priya@goodneighbor.com", "555-321-0004", "88 Claims Court", "Phoenix", "AZ", "85001"),
        ("Tom", "Bundleton", "tom@goodneighbor.com", "555-321-0005", "15 Home & Auto Dr", "Atlanta", "GA", "30301"),
    ]

    cursor.executemany("INSERT INTO user VALUES (?, ?, ?, ?, ?, ?, ?, ?)", starter_agents)
    conn.commit()



def list_names():
    print("ALL AGENT NAMES")
    print("-" * 10)
    cursor.execute("SELECT first_name, last_name FROM user")
    users = cursor.fetchall()
    for this_user in users:
        print(this_user[0], this_user[1])
    print(f"\nTotal agents: {len(users)}\n")

def list_contact_info():
    print("AGENT NAMES with Phone and Email")
    print("-" * 10)
    cursor.execute("SELECT first_name, last_name, phone, email FROM user")
    for this_user in cursor.fetchall():
        name = this_user[0] + " " + this_user[1]
        print(f"{name:<22}{this_user[2]:<15}{this_user[3]}")
    print()

def list_location():
    print("AGENT NAMES and Location")
    print("-" * 10)
    cursor.execute("SELECT first_name, last_name, city, state FROM user")
    for this_user in cursor.fetchall():
        name = this_user[0] + " " + this_user[1]
        print(f"{name:<22}{this_user[2]}, {this_user[3]}")


def add_user():
    print("Add New AGENT")
    print("-" * 10)
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email address: ")
    phone = input("Enter phone number: ")
    street = input("Enter street address: ")
    city = input("Enter city: ")
    state = input("Enter 2 digit state abbreviation: ").upper()
    zip_code = input("Enter zipcode: ")
 
    cursor.execute("INSERT INTO user VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (first_name, last_name, email, phone, street, city, state, zip_code))
    print(f"\n{first_name} {last_name} has been entered into the USER table.\n")

#MENU SCREEN

def menu():
    #state farm agents including jake from state farm meme
    print("We are Farmer!")
    print("\nChoose and option below:")
    print("1 - List the Names")
    print("2 - List the Names, Phone and Email")
    print("3 - List the Names and Location")
    print("4 - Add New User")
    print("5 - Exit the Program")
            

def main():
    while True:
        menu()
        choice = input("Please make a selection: ")
        print()
        if choice == "1":
            list_names()
        elif choice == "2":
            list_contact_info()
        elif choice == "3":
            list_location()
        elif choice == "4":
            add_user()
        elif choice == "5":
            break
        else:
            print("Not a valid option, Try Again!")

        conn.commit()

    conn.close()
    print("Thank you for using our database! :)")





if __name__ == "__main__":
    main()

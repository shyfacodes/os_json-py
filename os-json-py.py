import json
import os
#load 
#add
#update
#save
#delete
#search
#show_all
#exist
Detail = {}
def add_contact():
    
    Detail.update(load_contact())
    name = input("Enter your name: ")
    number = int(input("Enter your number: "))
    city = input("Enter your city: ")
    email = input("Enter your email: ")
    if name not in Detail:
        Detail[name] = {"phone": number, "city": city, "email": email}
        save_contact()
        print(Detail)
        print("Contact added successfully!")
    else: 
        print("Contact already exists.")

def load_contact():
    if os.path.exists("contacts.json"):
        with open("contacts.json", "r") as f:
            detail = json.load(f)
            return detail
        print("Contact loaded successfully!")
    else:
        return {}

def update_contact():
    Detail.update(load_contact())
    update_name = input("Enter the name of the contact you want to update: ")
    key_name = input("Enter the key you want to update (phone, city, email): ")
    if update_name in Detail:
        for updated_data in Detail[update_name].keys():
            if updated_data == key_name:
                new_value = input(f"Enter the new value for {key_name}: ")
                Detail[update_name][key_name] = new_value
                save_contact()
                break
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def save_contact():
    with open("contacts.json", "w") as f:
        json.dump(Detail, f, indent=4)
    print("Contact saved successfully!")


def delete_contact():
    Detail.update(load_contact())
    delete_name = input("Enter the name of the contact you want to delete: ")
    if delete_name in Detail:
        print(f"Details of {delete_name}: {Detail[delete_name]}")
        del Detail[delete_name]
        save_contact()


def search_contact():
    Detail.update(load_contact())
    search_name = input("Enter the name of the contact you want to search: ")
    if search_name in Detail:
        print(f"Details of {search_name}: {Detail[search_name]}")
    else :
        print("Contact not found.")

def show_all_contacts():
    Detail.update(load_contact())
    show_all = input("Do you want to show all contacts? (yes/no): ")
    if show_all.lower() == "yes":
        for name, details in Detail.items():
            print(f"Name: {name}, Phone: {details['phone']}, City: {details['city']}, Email: {details['email']}")



        
    
print("=" * 25)
print("\tCONTACT BOOK")
print("=" * 25)
print("1. Add Contact")
print("2. Update Contact")
print("3. Delete Contact")
print("4. Search Contact")
print("5. Show All Contact")
print("6. Exit")
while True:
    choice = input("Enter your choice(1-6): ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        update_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        search_contact()
    elif choice == "5":
        show_all_contacts()
    elif choice == "6":
        print("Exit")
        break
    else:
        print("Invalid Choice")
        print("Enter a valid choice")

   
print("="*25)
print()

print(Detail)
print(load_contact())
print(Detail)






































contacts = {}
contacts["Ahmed Ali"]  = {"phone": "03001234567", "city": "Karachi", "email": "ahmed@email.com"}
contacts["Sara Malik"] = {"phone": "03119876543", "city": "Lahore",  "email": "sara@email.com"}
contacts["Omar Khan"]  = {"phone": "03451112233", "city": "Islamabad", "email": "omar@email.com"}

contacts["Sara Malik"] ["city"]= "lahore"

value = contacts.get("Ahmed",{})
print(value.get("email","no phone saved"))
print(len(contacts))

# contact book 2 by def function



contacts = {}
def load_contact ():
    try:
        
        with open("contacts.json", "r") as me:
            contacts = json.load(f)
    except:
        contacts ={}
def save_contact():
    with open ("contact.json","w")as f:
        json.dump(contacts,f,indent = 4)

   
def add_contact ():

    name = input("Enter Contact Name: ")

    phone_no = input("Enter Contact Number: ")
    contacts[name] = phone_no
    save_contact()
    print("contact added successfully")

def search_contact ():

    search = input("Enter Contact Name: ")
    if search in contacts:
        print(f"{search} : {contacts[search]} ")
    else:
        print("contact not found")

def show_contact ():
    for name ,phone_no in contacts.items():
        print(f"{name} :{phone_no}")
load_contact()
print("=" * 25)
print("\tCONTACT BOOK")
print("=" * 25)
print("1. Add Contact")
print("2. Search Contact")
print("3. Show All Contact")
print("4. Exit")
while True:
    choice = input("Enter your choice(1-4): ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        show_contact()
    elif choice == "4":
        print("Exit")
        break
    else:
        print("Invalid Choice")
        print("Enter a valid choice")

   
print("="*25)
print()

# 1 contact book

contact = []
def add_contact ():
    name = input ("Enter name :")
    number = input ("Enter number :")
    contact.append  ({
        "name" : name,
        "number" : number
    })
def save_contact ():
    with open ("contacts.jason" ,"w") as f:
        json.dump(contact,f ,indent=4)


def load_contact ():
    try:
        with open ("contacts.json","r") as f:
            contact = json.load (f)
    except(FileNotFoundError):
        contact = []
        return
load_contact()
add_contact()
save_contact()
print(contact)
##access asignment

data = {

    "SHYFA": {"name": "SHYFA", "age": 20, "major": "Computer Science"},

    "MARWA": {"name": "MARWA", "age": 22, "major": "Mathematics"},

    "AROOBA": {"name": "AROOBA", "age": 21, "major": "Physics"},

    "ANAYA": {"name": "ANAYA", "age": 23, "major": "Chemistry"}
}
with open ("students.json", "w") as file:
    json.dump(data, file,indent=4)
with open ("students.json", "r") as file:
    loaded_data = json.load(file)
    print(json.dumps(loaded_data, indent=4))

print(f"{loaded_data['SHYFA']['name']} is {loaded_data['SHYFA']['age']} years old and majors in {loaded_data['SHYFA']['major']}.")
## practice
information={}
try:
    with open ("st_database.json","r") as S:
        information = json.load (S)
except FileNotFoundError:
        information ={}
        


roll_counter = len(information) + 1

while True:
    name=input("Enter your name: ")
    age=int(input("Enter your age: "))
    father_name=input("Enter your father's name: ")
    phone_number=input("Enter your phone number: ")
    address=input("Enter your address: ")

    student ={
        "st_name" :name,
        "st_age" :age,
        "st_father_name" :father_name,
        "st_phone_number" :phone_number,
        "st_address": address

    }
    duplicate = False
    for roll , info in information.items():
        if info["st_phone_number"] == phone_number:
            duplicate = True
            print(f"this student already exist in record [roll{roll}:{info['st_name']}]")
            break
    if not duplicate:

        roll_no =f"roll_{roll_counter:02d}"
        information[roll_no] = student 
        roll_counter +=1
        print("student has been added")
    more = input("would you want to add any more student data (yes/no)?")
    if more.lower()  != "yes":
        break
with open ("st_database.json","w") as S:
        json.dump(information , S , indent=4)
print (" all data would be added in st_database.")

       

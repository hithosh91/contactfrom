# Define the Contact class
class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def display(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}"

# Global list to store contacts
contacts = []

# Function to add a new contact
def add_contact():
    name = input("Please enter your name: ")
    phone = input("Please enter your phone number: ")
    email = input("Please enter your email: ")
    contact = Contact(name, email, phone)
    contacts.append(contact)
    print(" Contact added!")

# Function to view all contacts
def view_all():
    if not contacts:
        print(" No contacts in the list.")
    for c in contacts:
        print(c.display())

# Function to search for a contact
def search():
    search_name = input("Enter name to search: ")
    found = False
    for c in contacts:
        if c.name.lower() == search_name.lower():
            print(c.display())
            found = True
    if not found:
        print(" Contact not found.")

# Function to save contacts to a file
def save_contact(filename="contacts.txt"):
    with open(filename, "w") as f:
        for c in contacts:
            f.write(f"{c.name},{c.email},{c.phone}\n")
    print(" Contacts saved.")

# Function to load contacts from a file
def load_contact(filename="contacts.txt"):
    try:
        with open(filename, "r") as f:
            for line in f:
                name, email, phone = line.strip().split(",")
                contacts.append(Contact(name, email, phone))
        print(" Contacts loaded.")
    except FileNotFoundError:
        print(" No saved contacts found.")

# Main menu
def main():
    load_contact()
    while True:
        print("\n📘 --- Contact Book ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. View Contacts")
        print("4. Save & Exit")

        option = input("Please enter your choice (1-4): ")

        if option == "1":
            add_contact()
        elif option == "2":
            search()
        elif option == "3":
            view_all()
        elif option == "4":
            save_contact()
            print(" Goodbye!")
            break
        else:
            print(" Invalid option. Please try again.")

# Run the program
main()

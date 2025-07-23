# Contact book

contacts = []


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("✅ Contact added successfully.\n")


def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    print("\nContact List:")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    print()


def search_contact():
    term = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if term.lower() in contact['name'].lower() or term in contact['phone']:
            print("\nContact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
            found = True
    if not found:
        print("No matching contact found.\n")


def update_contact():
    term = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if term.lower() == contact['name'].lower():
            print("Leave blank to keep current value.")
            contact['name'] = input(f"New name ({contact['name']}): ") or contact['name']
            contact['phone'] = input(f"New phone ({contact['phone']}): ") or contact['phone']
            contact['email'] = input(f"New email ({contact['email']}): ") or contact['email']
            contact['address'] = input(f"New address ({contact['address']}): ") or contact['address']
            print("✅ Contact updated.\n")
            return
    print("Contact not found.\n")


def delete_contact():
    term = input("Enter the name of the contact to delete: ")
    for i, contact in enumerate(contacts):
        if term.lower() == contact['name'].lower():
            confirm = input(f"Are you sure you want to delete {contact['name']}? (y/n): ")
            if confirm.lower() == 'y':
                contacts.pop(i)
                print("🗑️ Contact deleted.\n")
            else:
                print("Deletion cancelled.\n")
            return
    print("Contact not found.\n")

def main_menu():
    while True:
        print("Contact Management System")
        print("=========================")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("👋 Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 6.\n")

main_menu()

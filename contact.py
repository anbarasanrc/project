contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added.")

def view_contacts():
    print("Contacts:")
    for i, contact in enumerate(contacts):
        print(i+1, contact["name"], contact["phone"], contact["email"])

def edit_contact():
    view_contacts()
    if contacts:
        contact_index = int(input("Enter contact number to edit: "))
        if contact_index > 0 and contact_index <= len(contacts):
            contact = contacts[contact_index-1]
            name = input("Enter new name (leave blank to keep current name): ")
            phone = input("Enter new phone number (leave blank to keep current phone number): ")
            email = input("Enter new email address (leave blank to keep current email address): ")
            if name:
                contact["name"] = name
            if phone:
                contact["phone"] = phone
            if email:
                contact["email"] = email
            print("Contact updated.")
        else:
            print("Invalid input.")
    else:
        print("No contacts to edit.")

def delete_contact():
    view_contacts()
    if contacts:
        contact_index = int(input("Enter contact number to delete: "))
        if contact_index > 0 and contact_index <= len(contacts):
            contacts.pop(contact_index-1)
            print("Contact deleted.")
        else:
            print("Invalid input.")
    else:
        print("No contacts to delete.")

# main program loop
while True:
    print("\nSelect option:")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Edit contact")
    print("4. Delete contact")
    print("5. Exit")

    option = input("Enter option number: ")

    if option == '1':
        add_contact()

    elif option == '2':
        view_contacts()

    elif option == '3':
        edit_contact()

    elif option == '4':
        delete_contact()

    elif option == '5':
        print("Exiting program.")
        break

    else:
        print("Invalid input.")

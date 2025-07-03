def is_valid_email(email):
    return '@' in email and '.' in email


def display_contacts(contact_book):
    if not contact_book:
        print(" No contacts to display.")
    else:
        print("\n Contact List:")
        for name, info in contact_book.items():
            print(f" {name}: Phone = {info['phone']}, Email = {info['email']}")


def contact_book_manager():
    contact_book = {}

    while True:
        print("\n Contact Book Menu:")
        print("1. Add New Contact")
        print("2. Update Existing Contact")
        print("3. Retrieve Contact")
        print("4. View All Contacts")
        print("5. Exit")

        choice = input(" Enter your choice (1-5): ")

        if choice == '1':
            name = input(" Enter contact name: ").strip().title()
            if name in contact_book:
                print(" Contact already exists!")
                continue

            phone = input(" Enter phone number: ").strip()
            email = input(" Enter email address: ").strip()

            if not is_valid_email(email):
                print(" Invalid email format. Must contain '@' and '.'")
                continue

            contact_book[name] = {"phone": phone, "email": email}
            print(f" Contact '{name}' added.")

        elif choice == '2':
            name = input(" Enter the name of contact to update: ").strip().title()
            if name not in contact_book:
                print(" Contact not found!")
                continue

            phone = input(" Enter new phone number: ").strip()
            email = input(" Enter new email address: ").strip()

            if not is_valid_email(email):
                print(" Invalid email format.")
                continue

            contact_book[name]["phone"] = phone
            contact_book[name]["email"] = email
            print(f" Contact '{name}' updated.")

        elif choice == '3':
            name = input(" Enter contact name to retrieve: ").strip().title()
            if name in contact_book:
                print(f" {name}: Phone = {contact_book[name]['phone']}, Email = {contact_book[name]['email']}")
            else:
                print(" Contact not found.")

        elif choice == '4':
            display_contacts(contact_book)

        elif choice == '5':
            print(" Exiting Contact Book. Goodbye!")
            break

        else:
            print(" Invalid choice. Please select between 1 and 5.")


# Run the contact book manager
if __name__ == "__main__":
    contact_book_manager()

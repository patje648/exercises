import re
class PhoneNumber:
    def __init__(self, number):
        self.number = number

class Contact:
    def __init__(self, name, email, numbers):
        self.name = name
        self.email = email
        self._numbers = numbers

    @property
    def numbers(self):
        return self._numbers

    @staticmethod
    def validate_email(email):
        # Regular expression for email validation
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

    @staticmethod
    def validate_number(number):
        # Check if at least one digit exists in the number
        return any(char.isdigit() for char in number)

    def validate_numbers(self):
        return all(self.validate_number(phone.number) for phone in self._numbers)

    def validate(self):
        if len(self.name) < 1:
            return False, "Name must be at least 1 character long."
        elif not self.validate_email(self.email):
            return False, "Invalid email format."
        elif not self.validate_numbers():
            return False, "At least one valid phone number is required."
        return True, "Contact validated successfully."

class ContactsManager:
    def __init__(self):
        self._contacts = []

    @property
    def contacts(self):
        return self._contacts

    def add_contact(self):
        name = input("Enter contact name: ")
        email = input("Enter contact email: ")
        phone = input("Enter contact phone number: ")
        
        for contact in self._contacts:
            if contact.name == name:
                print("Error: Contact with the same name already exists.")
                return
        
        self._contacts.append(Contact(name, email, phone))
        print("Contact added successfully.")

    def delete_contact(self):
        if not self._contacts:
            print("Error: No contacts to delete.")
            return
        
        name = input("Enter the name of the contact to delete: ")
        found = False
        for contact in self._contacts:
            if contact.name == name:
                self._contacts.remove(contact)
                found = True
                print("Contact deleted successfully.")
                break
        
        if not found:
            print("Error: Contact not found.")

    def find_contact(self, key):
        found_contacts = []
        for contact in self._contacts:
            if key.lower() in [contact.name.lower(), contact.email.lower(), contact.phone]:
                found_contacts.append(contact)
        
        if found_contacts:
            print("Found Contacts:")
            for contact in found_contacts:
                print(f"Name: {contact.name}, Email: {contact.email}, Phone: {contact.phone}")
        else:
            print("No contacts found.")

    def display_contacts(self, sort_by="name", order="ascending"):
        sorted_contacts = sorted(self._contacts, key=lambda x: getattr(x, sort_by.lower()))
        if order.lower() == "descending":
            sorted_contacts = sorted_contacts[::-1]
        
        print("Contacts:")
        for contact in sorted_contacts:
            print(f"Name: {contact.name}, Email: {contact.email}, Phone: {contact.phone}")
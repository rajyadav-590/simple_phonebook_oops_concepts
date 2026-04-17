class Contacts:
    phone_book = []

    def __init__(self, name, phone_no):
        self.name = name
        self.phone_no = phone_no
        Contacts.phone_book.append(self)

    def display(self):
        return f"Name: {self.name} and Phone no: {self.phone_no}"

    @classmethod
    def display_all(cls):
        for contact in cls.phone_book:
            print(contact.display())
        print("--------------------------")

    @classmethod
    def search_no(cls, search_name):
        for i in cls.phone_book:
            if i.name.strip().lower() == search_name.strip().lower():
                return i.phone_no
        return f"contact name: {search_name} is not found......."

    @staticmethod
    def number_validation(number_input):
        return number_input.isdigit() and 8 <= len(number_input) <= 10


print("welcome to phonebook..")
while True:
    print("1. for adding contacts")
    print("2. for displaying all contacts")
    print("3. for searching contact by name")
    print("4. Quit")
    print("--------------------------------")

    try:
        n = int(input("Enter your choice...."))

        if n == 1:
            name_input = input("Enter the name: ")
            number_input = input("Enter the number: ")

            if Contacts.number_validation(number_input):
                Contacts(name_input, number_input)
                print("your contact is added successfully")
            else:
                print("Number must be between 8 to 10 digits")

        elif n == 2:
            Contacts.display_all()

        elif n == 3:
            search_name = input("Enter the contact name to be searched: ")
            print(Contacts.search_no(search_name))
            print("----------------------------")

        elif n == 4:
            break

    except Exception:
        print("your input is wrong")
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
contact_1 = Contacts("ram",9876543210)
a = contact_1.display()
contact_1.display_all()
print(a)
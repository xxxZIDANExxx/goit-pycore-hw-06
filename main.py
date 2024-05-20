from collections import UserDict
from errors import InvalidName, InvalidPhone

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    
    def __init__(self, value):
        if not (value and isinstance(value, str)):
            raise InvalidName
        super().__init__(value)

class Phone(Field):
    # реалізація класу
    def __init__(self, value):
        if not (isinstance(value, str) and len(value)==10 and value.isdecimal()):
            raise InvalidPhone
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones:list[Phone] = []

    # реалізація класу
    def add_phone(self, phone:str):
        self.phones.append(Phone(phone))

    def remove_phone(self, del_phone:str):
        self.phones.remove(self.find_phone(del_phone))

    def edit_phone(self, old_phone:str, new_phone:str):
        old = self.find_phone(old_phone)
        if old:
            old.value = new_phone

    def find_phone(self, phone:str) -> Phone | None:
        phone = list(filter(lambda p: p.value==phone, self.phones))
        return phone[0] if phone else None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    #prints Record nicely in print(AddressBook)
    def __repr__(self) -> str:
        return self.__str__()

class AddressBook(UserDict):

    def add_record(self, record:Record):
        self.data[record.name.value] = record

    def find(self, record_name:str) -> Record:
        return self.data[record_name]

    def delete(self, record_name:str):
        del self.data[record_name]

def main():
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    john_record.add_phone("8888888888")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for _, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    john.remove_phone("8888888888")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

    print("Book",book)


if __name__ == "__main__":
       main()
import re
from collections import UserDict
from dataclasses import dataclass

PHONE_PATTERN = r"\d{3}"

@dataclass
class Field():
    value:any

    def __str__(self:"Field")->str:
        return str(self.value)
    
class Name(Field):
    def __init__(self,name:str)->None:
        super().__init__(name)

class Phone(Field):
    def __init__(self,phone:str)->None:
        self.value = phone
        self._validate()
        super().__init__(phone)

    def _validate(self):
        if not re.match(PHONE_PATTERN, self.value):
            raise ValueError(f"Invalid phone number: {self.value}. Use 10 digits")
        
        

class Record():
    def __init__(self,name:str)->None:
        self.name = Name(name)
        self.phones = list[Phone]() 
        self.birthday = None

    def add_phone(self,phone:str)->None:
        self.phones.append(Phone(phone))

    def remove_phone(self,phone:str)->None:
        self.phones.remove(Phone(phone))

    def edit_phone(self,old_phone:str,new_phone:str)->None:
        index = self.phones.index(Phone(old_phone))
        self.phones[index] = Phone(new_phone)
    def find_phone(self,phone:str)->str:
        return next((p.value for p in self.phones if p.value == phone), None)      

    def __str__(self:"Record")->str:
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"   

    def add_birthday(self,birthday:str)->None:
        self.birthday = BirthDay(birthday) 

class AddressBook(UserDict):   

    def add_record(self,record:Record)->None:
        self.data[record.name.value] = record

    def find(self,name:str)->Record:
        return self.data.get(name)
    
    def delete(self,name:str)->None:
        del self.data[name]

    def all_records(self)->list[Record]:        
        return list(self.data.values())

class BirthDay(Field):
    def __init__(self,value:str)->None:
        try:
            ...
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
    
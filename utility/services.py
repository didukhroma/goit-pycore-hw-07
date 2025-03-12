
from .input_err import input_error
from AddressBook import AddressBook, Record


@input_error
def add_contact(args:list, book: AddressBook)->str:
   
    if  not len(args) or len(args) != 2:
        raise ValueError("Please add all arguments: contact name and phone number for this command.")     
        
    name, phone, *_ = args
    record = book.find(name)
    message = f"Contact {name.capitalize()} updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = f"Contact {name.capitalize()} added."
    if phone:
        record.add_phone(phone)        
            
    return message

@input_error
def change_phone(args:list,book: AddressBook)->str:
    if not len(args) or len(args) != 3:
        raise ValueError("Please add all arguments: contact name, old phone number and new phone number for this command.")    
      
    name,old_phone,new_phone, *_ = args
    record = book.find(name)
    if record is None:
        raise KeyError("Please enter a valid name of contact.")
    record.edit_phone(old_phone,new_phone)
    return f"Contact {name.capitalize()} updated."

   

@input_error
def show_all(book: AddressBook)->str:
    contacts = book.all_records()   
    if not len(contacts):
        return "List is empty.Please add contacts"   

    return "\n".join([str(record) for record in contacts])
  

@input_error
def show_phone(args:list,book: AddressBook)->str:
    if not len(args) or len(args) != 1:
        raise ValueError("Please add all arguments: contact name for this command.")    
      
    name, *_ = args
    record = book.find(name)
    if record is None:
        raise KeyError("Please enter a valid name of contact.")
    return str(record)
    
@input_error
def add_birthday(args, book: AddressBook):
    pass
@input_error
def show_birthday(args, book: AddressBook):
    pass
@input_error  
def show_birthdays(args, book: AddressBook):
    pass
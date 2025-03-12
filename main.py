from utility import parse_input,add_contact,change_phone,show_all,show_phone,add_birthday,show_birthday,show_birthdays
from AddressBook import AddressBook, Record

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        
        command, args = parse_input(user_input)

        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        
        elif command == "hello":
            print("How can I help you?")
        
        elif command == "add":
            print(add_contact(args, book))
        
        elif command == "change":
            print(change_phone(args, book))
        
        elif command == "phone":
            print(show_phone(args, book))
        
        elif command == "all":
            print(show_all(book))
        # in progress
        elif command == "add-birthday":
            print(add_birthday(args, book))
        # in progress
        elif command == "show-birthday":
            print(show_birthday(args, book))
        # in progress
        elif command == "birthdays":
            print(show_birthdays(book))
        
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()



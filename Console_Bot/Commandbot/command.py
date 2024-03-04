
from Fieldbot.field import Birthday
from Functionbot import func


def main():    
    book = func.load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = func.parse_input(user_input)
        if command in ["close", "exit"]:
            user_change = input("Save change? y/n: ")
            user_change = user_change.lower()
            if user_change == "y":
                print(func.save_data(book))
            print('goodbye:)')
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
           print(func.add_contact(args, book))
        elif command == "change":
            print(func.change_contact(args, book))
        elif command == "phone":
            print(func.show_contacts(args, book))
        elif command == "all":
            print(book)        
        elif command == "delete":
            print(func.del_contact(args, book))
        elif command == "add_birthday":
             print(func.add_birthday(args, book))
        elif command == "show_birthday":
             print(func.show_birthday(args, book))
        elif command == "birthdays":
             print(Birthday(book))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

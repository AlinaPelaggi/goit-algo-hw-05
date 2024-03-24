#Четверте завдання
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def wrapper(*args, **kwards):
        try:
            return func(*args, **kwards)
        except (KeyError, ValueError, IndexError) as e:
            error_message = {
                KeyError: "Please enter user name",
                ValueError: "Enter name and phone number please",
                IndexError: "Invalis index. Please try again"
            }
            print(error_message.get(type(e), "Error accured. Please try again."))
            return wrapper

@input_error  
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error  
def change_contact(args, contacts):
    name, phone = args
    if contacts.get(name):
        contacts[name] = phone
        return "Contact changed."
    else:
        return "Conctact not exist"

@input_error  
def show_phone(args, contacts):
    name = args[0]
    contacts_phone = contacts.get(name)
    if contacts_phone:
        return contacts_phone
    else:
        return "Conctact not exist"

def show_all(contacts):
    return contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command =='change':
            print(change_contact(args,contacts))
        elif command == "phone":
            print(show_phone(args,contacts))    
        elif command == "all":
            print(show_all(contacts))    
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
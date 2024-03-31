#Четверте завдання
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "The contact exists"
        except ValueError:
            return "Please enter the correct arguments"
        except IndexError:
            return "No such contacts"
    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    if not args or len(args) != 2:
        raise ValueError
    name, phone = args
    if name in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if not args or len(args) != 2:
        raise ValueError
    name, phone = args
    if name not in contacts:
        raise IndexError
    contacts[name] = phone
    return "Contact updated successfully"

@input_error
def show_contact(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[args[0]] 
    else:
        raise IndexError

@input_error
def show_all(contacts):
    if not contacts:
        raise IndexError
    all_contacts = []
    for name in contacts:
        all_contacts.append(f'{name}: {contacts[name]}')
        
    return '\n'.join(all_contacts)
    
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
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_contact(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()

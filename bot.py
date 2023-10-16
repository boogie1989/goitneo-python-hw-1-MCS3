def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def hello_command(args, contacts):
    return "How can I help you?"

def add_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        if name in contacts:
            return f"Contact {name} exists. For an update, use the 'change' command."
        contacts[name] = phone
        return "Contact added."
    else:
        return "Invalid command. Please use 'add username phone'."

def change_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "Contact updated."
        else:
            return "Contact not found."
    else:
        return "Invalid command. Please use 'change username phone'."

def remove_contact(args, contacts):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            del contacts[name]
            return f"Contact {name} deleted."
        else:
            return f"Contact {name} not found."
    else:
        return "Invalid command. Please use 'delete username'."

def get_phone(args, contacts):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return "Contact not found."
    else:
        return "Invalid command. Please use 'phone username'."

def show_all(args, contacts):
    contact_strings = []
    if contacts:
        for name, phone in contacts.items():
            contact_strings.append(f"{name}: {phone}")
    else:
        contact_strings.append("No contacts found.")
    return contact_strings

COMMAND_HELLO = "hello"
COMMAND_ADD = "add"
COMMAND_CHANGE = "change"
COMMAND_REMOVE = "remove"
COMMAND_PHONE = "phone"
COMMAND_ALL = "all"
COMMAND_CLOSE = "close"
COMMAND_EXIT = "exit"

command_functions = {
    COMMAND_HELLO: hello_command,
    COMMAND_ADD: add_contact,
    COMMAND_CHANGE: change_contact,
    COMMAND_REMOVE: remove_contact,
    COMMAND_PHONE: get_phone,
    COMMAND_ALL: show_all,
}

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in [COMMAND_CLOSE, COMMAND_EXIT]:
            print("Good bye!")
            break
        elif command in command_functions:
            print(command_functions[command](args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()






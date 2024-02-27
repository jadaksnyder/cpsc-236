def display():
    print("Contact Manager")
    
contacts = ["Guido van Rossum", "guido@python.org", "+31 10 714 6100"],
["Eric Idle", "eric@ericidle.com", "+44 20 7946 0958"]

def display_contacts():
    print("Command: List")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contacts[0]}")

def view_contact(index):
    try: 
        contact = contacts[index - 1]
        print(f"Command: view\nNumber: {index}\nName: {contact[0]}\nEmail: {contact[1]}\nPhone: {contact[2]}")
    except IndexError:
        print("Invalid contact number. Please enter a valid number.")

def add_contact(name, email, phone):
    contacts.append([name, email, phone])
    print(f"Command: add\n{name} was added.")
    
def add_delete_contact(index):
    try:
        deleted_contact = contacts.pop(index - 1)
        print(f"Command: del\nNumber: {index}\n{deleted_contact[0]} was deleted.")
    except IndexError:
        print("Invalid contact number. Please enter a valid number.")        
        
def contact_manager():
    print("Contact Manager\n")
    while True:
        print("COMMAND MENU\nlist - Display all contacts\nview - View a contact\nadd - Add a contact\ndel - Delete a contact\nexit - Exit program")
        command = input("Command: ").lower()
        
        if command == 'list':
            display_contacts()
        
        elif command == 'view':
            index = int(input("Number: "))
            view_contact(index)
            
        elif command == 'add':
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            add_contact(name, email, phone)
        
        elif command == 'del':
            index = int(input("Number: "))
            add_delete_contact(index)
         
        elif command == 'exit':
            print("Bye!")
            break
        
        else:
            print("Invalid command. Please enter a valid command.")
            
if __name__ == "__main__":
    contact_manager()
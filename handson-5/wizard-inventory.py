import random

# File name for storing items carried by the wizard
WIZARD_INVENTORY_FILE = "wizard_inventory.txt"

def show_items():
    try:
        with open(WIZARD_INVENTORY_FILE, "r") as file:
            items = file.readlines()
            if items:
                print("Wizard Inventory:")
                for idx, item in enumerate(items, start=1):
                    print(f"{idx}. {item.strip()}")
            else:
                print("Wizard Inventory is empty.")
    except FileNotFoundError:
        print("Wizard Inventory is empty.")

def grab_item():
    try:
        with open(WIZARD_INVENTORY_FILE, "r") as file:
            current_items = file.readlines()
            if len(current_items) >= 4:
                print("You can't carry any more items. Drop something first.")
                return
    except FileNotFoundError:
        current_items = []

    item = input("While walking down a path, you see: ").strip()
    
    with open(WIZARD_INVENTORY_FILE, "a") as file:
        file.write(item + "\n")
    
    print(f"You picked up {item}.")

def drop_item():
    try:
        with open(WIZARD_INVENTORY_FILE, "r") as file:
            current_items = file.readlines()
    except FileNotFoundError:
        print("Wizard Inventory is empty.")
        return
    
    if not current_items:
        print("Wizard Inventory is empty.")
        return
    
    print("Wizard Inventory:")
    for idx, item in enumerate(current_items, start=1):
        print(f"{idx}. {item.strip()}")

    try:
        choice = int(input("Drop Number: "))
        if 1 <= choice <= len(current_items):
            dropped_item = current_items.pop(choice - 1)
            with open(WIZARD_INVENTORY_FILE, "w") as file:
                file.writelines(current_items)
            print(f"You dropped {dropped_item.strip()}.")
        else:
            print("Invalid item number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    print("The Wizard Inventory Program\n")
    while True:
        print("COMMAND MENU")
        print("walk - Walk down the path")
        print("show - Show all items")
        print("drop - Drop an item")
        print("exit - Exit program")
        
        command = input("\nCommand: ").strip().lower()
        if command == "walk":
            grab_item()
        elif command == "show":
            show_items()
        elif command == "drop":
            drop_item()
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()



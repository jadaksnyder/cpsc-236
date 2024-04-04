def display():
    print("Favorite Foods Tracker")
    print("Choose an option: ")
    print("1. Show Favorite Foods")
    print("2. Add a Favorite Food")
    print("3. Remove a Favorite Food")
    print("4. Exit")
    
favorite_foods = []

def display_favorite_foods():
    print("1. Show Favorite Foods")
    for i, favorite_foods in enumerate(favorite_foods, 1):
        print(f"{i}. {favorite_foods([0])}")

def add_favorite_food():
    new_food = input("Enter a food to add: ")
    favorite_foods.append([new_food])
    print(f"{new_food} added to your favorite foods.")

def remove_favorite_food(index):
    remove_food = input("Enter a food to remove: ")
    remove_food = favorite_foods.pop(index - 1)
    print(f"{remove_food} removed from your favorite foods.")
    
def exit(user_choice):
    if user_choice == '4':
        exit()

def main():
    
    
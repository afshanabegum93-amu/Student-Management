inventory = {}

def add_ingredient():
    name = input("Enter ingredient name: ").lower()
    if name in inventory:
        print(f"{name.title()} already exists. Use update to change quantity.")
        return
    quantity = input("Enter quantity ('10 kilos''5 kilos'): ")
    inventory[name] = quantity
    print(f"{name.title()} added with quantity {quantity}.")

def view_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    print("Current Inventory:")
    for name, qty in inventory.items():
        print(f"{name.title()}: {qty}")

def update_ingredient():
    name = input("Enter ingredient to update: ").lower()
    if name not in inventory:
        print("Ingredient not found.")
        return
    quantity = input("Enter new quantity: ")
    inventory[name] = quantity
    print(f"{name.title()} updated to {quantity}.")

def search_ingredient():
    name = input("Enter ingredient name to search: ").lower()
    if name in inventory:
        print(f"{name.title()}: {inventory[name]}")
    else:
        print("Ingredient not found.")

def main():
    while True:
        print("\n--- Bakery Inventory Menu ---")
        print("1. Add Ingredient")
        print("2. View Inventory")
        print("3. Update Ingredient")
        print("4. Search Ingredient")
        print("5. Exit")
        choice = input("Enter choice (1-5): ")

        if choice == '1':
            add_ingredient()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            update_ingredient()
        elif choice == '4':
            search_ingredient()
        elif choice == '5':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")

main()

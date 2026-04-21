#Main I guess bro

import pickle
from retailitem import RetailItem
from cashregister import CashRegister

INVENTORY_FILE = "inventory.dat"
PASSWORD = "admin123"



# Yuhtility Func

def load_inventory():
    inventory = {}

    try:
        file = open(INVENTORY_FILE, "rb")
        inventory = pickle.load(file)
        file.close()
    except:
        inventory = {}

    return inventory


def save_inventory(inventory):
    try:
        file = open(INVENTORY_FILE, "wb")
        pickle.dump(inventory, file)
        file.close()
    except:
        print("Error saving inventory.")


def validate_int(prompt):
    valid = False
    value = 0

    while not valid:
        user_input = input(prompt)

        try:
            value = int(user_input)
            valid = True
        except:
            print("Invalid input. Enter a whole number.")

    return value


def validate_float(prompt):
    valid = False
    value = 0.0

    while not valid:
        user_input = input(prompt)

        try:
            value = float(user_input)
            valid = True
        except:
            print("Invalid input. Enter a numeric value.")

    return value



# Inventory System I guess bro

def inventory_menu():
    password = input("Enter password: ")

    if password == PASSWORD:
        inventory = load_inventory()
        done = False

        while not done:
            print("\n--- Inventory Menu ---")
            print("1. Display Inventory")
            print("2. Add Item")
            print("3. Save Inventory")
            print("4. Exit")

            choice = input("Select option: ")

            if choice == "1":
                if len(inventory) == 0:
                    print("Inventory is empty.")
                else:
                    for key in inventory:
                        print(f"{key}: {inventory[key]}")

            elif choice == "2":
                desc = input("Enter item description: ")
                units = validate_int("Enter units (how many): ")
                price = validate_float("Enter price: ")

                item_id = len(inventory) + 1
                inventory[item_id] = RetailItem(desc, units, price)

                print("Item added.")

            elif choice == "3":
                save_inventory(inventory)
                print("Inventory saved.")

            elif choice == "4":
                done = True

            else:
                print("Invalid choice.")
    else:
        print("Incorrect password.\n")




# Retail System bruh

def retail_menu():
    inventory = load_inventory()
    register = CashRegister()
    done = False

    while not done:
        print("\n--- Retail Menu ---")
        print("1. Display Cart")
        print("2. Display Items")
        print("3. Purchase Item")
        print("4. Empty Cart")
        print("5. Checkout")
        print("6. Exit to Main Menu")

        choice = input("Select option: ")

        if choice == "1":
            register.get_cart()

        elif choice == "2":
            if len(inventory) == 0:
                print("No inventory available.")
            else:
                for key in inventory:
                    print(f"{key}: {inventory[key]}")

        elif choice == "3":
            if len(inventory) == 0:
                print("No items available.")
            else:
                item_id = validate_int("Enter item number: ")

                if item_id in inventory:
                    item = inventory[item_id]

                    if item.get_units() > 0:
                        register.purchase_item(item)
                        item.set_units(item.get_units() - 1)
                        print("Item added to cart.")
                    else:
                        print("Item out of stock.")
                else:
                    print("Invalid item number.")

        elif choice == "4":
            register.empty()
            print("Cart emptied.")

        elif choice == "5":
            register.get_cart()
            total = register.get_total()
            print(f"\nTotal: ${total:.2f}")

            confirm = input("Confirm purchase? (y/n): ")

            if confirm.lower() == "y":
                save_inventory(inventory)
                register.empty()
                print("Purchase complete.\n")
                done = True

        elif choice == "6":
            done = True

        else:
            print("Invalid choice.")



# Main Menu i guess bro

def main():
    done = False

    while not done:
        print("\n=== ACME Retail System ===")
        print("1. Inventory System")
        print("2. Retail System")
        print("3. Exit")

        choice = input("Select option: ")

        if choice == "1":
            inventory_menu()

        elif choice == "2":
            retail_menu()

        elif choice == "3":
            print("Goodbye.")
            done = True

        else:
            print("Invalid selection.")
            
            
            
            
            
            
            
            
            
            
            
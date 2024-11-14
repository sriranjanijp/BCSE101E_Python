#4. Product Inventory Management (Sets)
#Design a menu-driven program using user-defined functions to manage a store's product inventory. Each product's name is stored in a set. The program should allow the user to:
#- Add a new product to the inventory
#- Remove a product from the inventory
#- Check if a product is in stock
#- Display all available products
#- Compare two inventories (sets) and display products unique to each
#- Display products available in both sets (common products between two stores)
#- Find and display products that are in one set but not the other
import random
# Add a new product to the inventory
def addProduct(inventory, product):
    inventory.add(product)
    return inventory

# Remove a product from the inventory
def removeProduct(inventory, product):
    inventory.discard(product)  # Using discard to avoid errors if product is not in the set
    return inventory

# Check if a product is in stock
def isInStock(inventory, product):
    return product in inventory

# Display all available products
def displayInventory(inventory):
    print("Current inventory:", inventory)

# Compare two inventories and display products unique to each
def uniqueProducts(inventory1, inventory2):
    unique_to_inventory1 = inventory1 - inventory2
    unique_to_inventory2 = inventory2 - inventory1
    return unique_to_inventory1, unique_to_inventory2

# Display products available in both sets (common products between two stores)
def commonProducts(inventory1, inventory2):
    return inventory1 & inventory2

# Find and display products that are in one set but not the other (symmetric difference)
def exclusiveProducts(inventory1, inventory2):
    return inventory1 ^ inventory2

inventory_a = {"apple", "banana", "cherry", "dates", "kiwi"}
inventory_b = {"banana", "kiwi", "mango", "orange", "pineapple"}

while True:
    print("1: Add a new product to the inventory")
    print("2: Remove a product from the inventory")
    print("3: Check if a product is in stock")
    print("4: Display all available products")
    print("5: Compare two inventories and show unique products")
    print("6: Display common products between two inventories")
    print("7: Display products exclusive to each inventory (symmetric difference)")

    choice = random.randint(1,8)
    
    if choice == 1:
        print("Enter the product name to add: apple")
        product = 'apple'
        print("Inventory after addition:", addProduct(inventory_a, product))
        break
    elif choice == 2:
        print("Enter the product name to remove: apple")
        product = 'apple'
        print("Inventory after removal:", removeProduct(inventory_a, product))
        break
    elif choice == 3:
        print("Enter the product name to check: apple")
        product = 'apple'
        if isInStock(inventory_a, product):
            print(f"{product} is in stock.")
        else:
            print(f"{product} is not in stock.")
        break
    elif choice == 4:
        displayInventory(inventory_a)
        break
    elif choice == 5:
        unique_to_a, unique_to_b = uniqueProducts(inventory_a, inventory_b)
        print("Products unique to inventory A:", unique_to_a)
        print("Products unique to inventory B:", unique_to_b)
        break
    elif choice == 6:
        print("Common products between inventory A and B:", commonProducts(inventory_a, inventory_b))
        break
    elif choice == 7:
        print("Products exclusive to either inventory A or B:", exclusiveProducts(inventory_a, inventory_b))
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 8.")

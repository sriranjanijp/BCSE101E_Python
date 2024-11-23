import random
# Add a key-value pair to the dictionary
def addKeyValue(d, key, value):
    d[key] = value
    return d

# Update the value of an existing key
def updateValue(d, key, value):
    if key in d:
        d[key] = value
        print(f"Updated {key} to {value}.")
    else:
        print(f"Key '{key}' does not exist.")
    return d

# Delete a key-value pair
def deleteKey(d, key):
    if key in d:
        del d[key]
        print(f"Deleted key '{key}'.")
    else:
        print(f"Key '{key}' does not exist.")
    return d

# Check if a key exists in the dictionary
def keyExists(d, key):
    return key in d

# Get the value associated with a key
def getValue(d, key):
    return d.get(key, "Key not found.")

# Display all keys in the dictionary
def displayKeys(d):
    print("Keys:", list(d.keys()))

# Display all values in the dictionary
def displayValues(d):
    print("Values:", list(d.values()))

# Display all key-value pairs in the dictionary
def displayItems(d):
    print("Key-Value Pairs:", d)

# Initialize a dictionary with some sample key-value pairs
dictionary = {
    "apple": 10,
    "banana": 20,
    "cherry": 15,
    "date": 30,
    "fig": 25
}

# Predefined values for demonstration
key_to_add = "grape"
value_to_add = 35
key_to_update = "banana"
new_value = 22
key_to_delete = "date"
key_to_check = "apple"
key_to_get_value = "cherry"

# Menu-driven program with predefined inputs
while True:
    print("\nDictionary Operations Menu")
    print("1: Add a key-value pair to the dictionary")
    print("2: Update the value of an existing key")
    print("3: Delete a key-value pair")
    print("4: Check if a key exists in the dictionary")
    print("5: Get the value associated with a key")
    print("6: Display all keys in the dictionary")
    print("7: Display all values in the dictionary")
    print("8: Display all key-value pairs in the dictionary")
    
    choice = random.randint(1,15)

    if choice == 1:
        print(f"Adding key '{key_to_add}' with value {value_to_add}.")
        addKeyValue(dictionary, key_to_add, value_to_add)
        print("Dictionary after addition:", dictionary)
        break
    elif choice == 2:
        print(f"Updating key '{key_to_update}' with new value {new_value}.")
        updateValue(dictionary, key_to_update, new_value)
        break
    elif choice == 3:
        print(f"Deleting key '{key_to_delete}'.")
        deleteKey(dictionary, key_to_delete)
        break
    elif choice == 4:
        if keyExists(dictionary, key_to_check):
            print(f"Key '{key_to_check}' exists in the dictionary.")
        else:
            print(f"Key '{key_to_check}' does not exist.")
        break
    elif choice == 5:
        print(f"Getting value for key '{key_to_get_value}'.")
        print("Value:", getValue(dictionary, key_to_get_value))
        break
    elif choice == 6:
        displayKeys(dictionary)
        break
    elif choice == 7:
        displayValues(dictionary)
        break
    elif choice == 8:
        displayItems(dictionary)
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 9.")
        choice = random.randint(1,8)

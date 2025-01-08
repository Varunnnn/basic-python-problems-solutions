"""
Problem - 

Write a Python program to:
Create a dictionary with five key-value pairs.
Add, update, and delete an element in the dictionary.

Let's do it

"""

my_dict = {}

def add_word():
    dict_size = int(input("Enter the number of elements to add: "))
    for _ in range(dict_size):
        key = input("Enter the key: ")
        value = input("Enter the value for the key: ")
        my_dict[key] = value
    print("\nDictionary after addition:", my_dict)


def update_dict():
    key = input("Enter the key to update: ")
    if key in my_dict:
        value = input("Enter the new value for the key: ")
        my_dict[key] = value
        print("\nDictionary after update:", my_dict)
    else:
        print(f"\nKey '{key}' not found in the dictionary.")

def delete_dict():
    key = input("Enter the key to delete: ")
    if key in my_dict:
        del my_dict[key]
        print("\nDictionary after deletion:", my_dict)
    else:
        print(f"\nKey '{key}' not found in the dictionary.")

def display_menu():
    print("\nSelect an option:")
    print("1. Add elements to the dictionary")
    print("2. Update an element in the dictionary")
    print("3. Delete an element from the dictionary")
    print("4. Exit")


while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")
    match choice:
        case "1":
            add_word()
        case "2":
            update_dict()
        case "3":
            delete_dict()
        case "4":
            print("Exiting the program. Goodbye!")
            break
        case _:
            print("Invalid choice. Please try again.")

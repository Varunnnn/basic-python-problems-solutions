"""
Problem statement -

Create a program that counts the frequency of each character in a string using a dictionary.

Let's do it.

"""

user_input = input("Enter a string: ")

char_count = {}

for char in user_input:
    if char not in char_count:
        char_count[char] = 1  # Initialize count if character is not in dictionary
    else:
        char_count[char] += 1  # Increment count if character is already in dictionary

print(char_count)

"""
Problem statement - 

Create a function that accepts a list of numbers and returns a new list with only the even numbers.

Let's do it ... 

"""

list_size = int(input("Enter the size of the list: "))

num_list = []

for _ in range(0, list_size):
    list_element = int(input("Enter the element:"))
    num_list.append(list_element)

#print(num_list)

def list_fun(num_list):
  even_list = []
  for i in range(0, len(num_list)):
    if num_list[i] % 2 == 0:
      even_list.append(num_list[i])
  return print(even_list)

list_fun(num_list)

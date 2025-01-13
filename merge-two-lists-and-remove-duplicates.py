"""
Problem Statement - 

Create a program that merges two lists and removes duplicates.

Let's do it
"""

list_first = [1,2,3,4,5,6,7,8]
list_second = [4,5,6,7,8,9,10,11]

def merge_lists(list_a, list_b):
  new_list = list_a + list_b
  print('merged_list :', new_list)
  unique_list = []
  for i in range(len(new_list)):
    if new_list[i] not in unique_list:
      unique_list.append(new_list[i])
  print('List after duplicates removed : ', unique_list)

merge_lists(list_first, list_second)

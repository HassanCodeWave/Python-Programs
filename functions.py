# Develop a Python function that takes a list as a parameter and returns a list with 
# unique values from the provided link 
# Example: 
# if given list a [ 1,1,2,2,2,2,3,4,4,5,6,6,7 ]
# It should return a list as [ 1,2,3,4,5,6,7 ].
def unique_list(list):
 newlist = []
 for i in list:
 if i not in newlist:
 newlist.append(i):
 else:
 pass
 return newlist
list = [1, 1, 2, 2, 2, 2, 3, 4, 4, 5, 6, 6, 7]
print(unique_list(list))

# Write a program to print the smallest number in a given list and its location 
# index.
def find_smallest_number(numbers):
 smallest = numbers[0]
 index = 0
 for i in range(1, len(numbers)):
 if numbers[i] < smallest:
 smallest = numbers[i]
 index = i
 return smallest, index
number_list = [1.2, 3.0, 4.2, 6.1, 5.3, 7.4, 9.9, 8.5]
smallest_num, smallest_index = find_smallest_number(number_list)
print("Smallest number:", smallest_num)
print("Index of smallest number:", smallest_index)

# Extend the program of Q2(a) to interchange (swap) the first number and the 
# location at which smallest values is formed. 
def find_smallest_number(numbers):
 smallest = numbers[0]
 index = 0
 for i in range(1, len(numbers)):
 if numbers[i] < smallest:
 smallest = numbers[i]
 index = i
 return smallest, index
def swap_first_with_smallest(numbers):
 smallest, index = find_smallest_number(numbers)
 numbers[0], numbers[index] = numbers[index], numbers[0]
 return numbers
number_list = [1.2, 3.0, 4.2, 6.1, 5.3, 7.4, 9.9, 8.5]
smallest_num, smallest_index = find_smallest_number(number_list)
print("Smallest number:", smallest_num)
print("Index of smallest number:", smallest_index)
swapped_list = swap_first_with_smallest(number_list)
print("List after swapping:", swapped_list)

# Write a python program to sort a given list of numbers by using the selection 
# sort algorithm
def selection_sort(numbers):
 n = len(numbers)
 for i in range(n):
 min_idx = i
 for j in range(i+1, n):
 if numbers[j] < numbers[min_idx]:
 min_idx = j
 numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
 return numbers
number_list = [7, 2, 5, 1, 9, 3]
sorted_list = selection_sort(number_list)
print("Sorted list:", sorted_list)


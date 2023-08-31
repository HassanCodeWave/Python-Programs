# Reverse a list in python, list can be assumed.
list = [1,2,3,4,5]
list.reverse()
print(list)

# Concatenates two list, list can be assumed.
list1 = [1,2,3]
list2 = [4,5,6]
print(list1+list2)

# Turn every item of a list into it’s square.
list = [1,2,3,4,5]
newlist = []
for i in list:
 newlist.append(i**2)
print(newlist)

# Remove the empty strings from the list of strings.
list = ['Pakistan','','Japan','','USA','','Turkey']
for i in list:
 if i =='':
 del list[list.index(i)]
print(list)

# Remove all occurrences of a specific item from list.
list = [5,20,15,20,25,50,20]
for i in list:
 if i == 20:
 list.remove(i)
print(list)


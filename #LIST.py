#LIST
#It is a built in data types which is used to store set of values
#It can store data of different types(integer,float,string etc)
#It is mututable

# Creating a list
lst = [10, 20, 30, 20]

print("Original list:", lst)

lst.append(40)            # Adds 40 at the end of the list
print("After append:", lst)

lst.extend([50, 60])      # Adds multiple elements to the list
print("After extend:", lst)

lst.insert(1, 15)         # Inserts 15 at index 1
print("After insert:", lst)

lst.remove(20)            # Removes first occurrence of 20
print("After remove:", lst)

x = lst.pop(2)            # Removes and returns element at index 2
print("Popped element:", x)
print("After pop:", lst)

count_20 = lst.count(20) # Counts how many times 20 occurs in the list
print("Count of 20:", count_20)

idx = lst.index(30)       # Returns index of first occurrence of 30
print("Index of 30:", idx)

lst.sort()                # Sorts the list in ascending order
print("After sort:", lst)

lst.reverse()             # Reverses the order of the list
print("After reverse:", lst)

new_lst = lst.copy()      # Creates a shallow copy of the list
print("Copied list:", new_lst)

lst.clear()               # Removes all elements from the list
print("After clear:", lst)


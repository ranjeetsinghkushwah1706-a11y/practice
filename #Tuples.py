#Tuples
# A tuple is an ordered collection of elements enclosed in parentheses ().
# Tuples are immutable, meaning their values cannot be changed after creation.
# Tuples can store different data types (int, float, string, etc.).
# Tuples allow duplicate values.
# Tuples are faster than lists and use less memory.
# Tuples support indexing and slicing like lists.
# Tuples can be nested inside other tuples.
# A tuple with one element must have a comma: (10,).
# Tuples are often used for fixed data that should not be modified.
# Tuples can be unpacked into variables

# Creating a tuple
# Creating a tuple
t = (10, 20, 30, 10, 40, 10)
print("Original tuple:", t)

c = t.count(10)              # Counts how many times 10 appears in the tuple
print("Count of 10:", c)

i = t.index(30)              # Finds index of first occurrence of 30
print("Index of 30:", i)

l = len(t)                   # Returns total number of elements
print("Length of tuple:", l)

mx = max(t)                  # Returns maximum value from the tuple
print("Maximum value:", mx)

mn = min(t)                  # Returns minimum value from the tuple
print("Minimum value:", mn)

s = sum(t)                   # Returns sum of all elements
print("Sum of elements:", s)

st = sorted(t)               # Sorts tuple and returns a new list
print("Sorted tuple (as list):", st)

chk = 20 in t                # Checks if 20 is present in the tuple
print("Is 20 in tuple?:", chk)

sl = t[1:4]                  # Slices elements from index 1 to 3
print("Sliced tuple:", sl)

a, b, c, d, e, f = t         # Unpacks tuple into variables
print("Unpacked values:", a, b, c, d, e, f)

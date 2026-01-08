# Creating a set
s = {10, 20, 30, 40}
print("Original set:", s)

s.add(50)                      # Adds 50 to the set
print("After add:", s)

s.update([60, 70])             # Adds multiple elements to the set
print("After update:", s)

s.remove(20)                   # Removes 20 (error if not present)
print("After remove:", s)

s.discard(100)                 # Removes 100 if present (no error if absent)
print("After discard:", s)

p = s.pop()                    # Removes and returns a random element
print("Popped element:", p)
print("After pop:", s)

s2 = {30, 40, 80}
print("Second set:", s2)

u = s.union(s2)                # Returns union of both sets
print("Union:", u)

i = s.intersection(s2)         # Returns common elements
print("Intersection:", i)

d = s.difference(s2)           # Returns elements in s but not in s2
print("Difference:", d)

sd = s.symmetric_difference(s2)# Returns elements not common in both sets
print("Symmetric difference:", sd)

s.clear()                      # Removes all elements from the set
print("After clear:", s)

#Dictionary

# Creating a dictionary
d = {"a": 10, "b": 20, "c": 30}
print("Original dictionary:", d)

v = d.get("b")                 # Returns value for key 'b'
print("Value of key 'b':", v)

k = d.keys()                   # Returns all keys
print("Keys:", k)

val = d.values()               # Returns all values
print("Values:", val)

it = d.items()                 # Returns all key-value pairs
print("Items:", it)

d.update({"d": 40})            # Adds new key-value pair
print("After update:", d)

p = d.pop("a")                 # Removes key 'a' and returns its value
print("Popped value:", p)
print("After pop:", d)

last = d.popitem()             # Removes and returns last inserted item
print("Popped last item:", last)
print("After popitem:", d)

d.setdefault("e", 50)          # Adds key 'e' with value 50 if not present
print("After setdefault:", d)

copy_d = d.copy()              # Creates a shallow copy of dictionary
print("Copied dictionary:", copy_d)

d.clear()                      # Removes all items from dictionary
print("After clear:", d)

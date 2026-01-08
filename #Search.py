# Search
tuple1 = (2, 4, 9, 16, 25, 36, 49, 64, 72, 81, 100)
count = 0

x = int(input("Enter number to be searched: "))

for item in tuple1:
    if item == x:
        count += 1

if count > 0:
    print("Number exists")
else:
    print("Number does not exist")

print("Count =", count)


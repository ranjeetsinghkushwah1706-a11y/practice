#Count occurance
lst = [1, 2, 3, 2, 4, 2]
x = int(input("Enter element to count: "))

count = 0
for item in lst:
    if item == x:
        count += 1

print("Count =", count)

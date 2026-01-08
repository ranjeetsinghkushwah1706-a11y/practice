# for loop search
lst = [1, 4, 9, 16, 25, 36, 49, 64]
found = False

x = int(input("Enter number: "))

for i in range(len(lst)):
    if lst[i] == x:
        print("Number found:", lst[i], "at index", i)
        found = True
        break

if not found:
    print("Number not found")

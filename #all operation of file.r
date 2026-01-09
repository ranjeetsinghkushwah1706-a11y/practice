#all operation of file

import os

filename = "demo_file.txt"

print("---- FILE HANDLING OPERATIONS START ----\n")

# 1. Create & Write to file
with open(filename, "w") as f:
    f.write("Hello World\n")
    f.write("Python File Handling\n")
print("1. File created and written.")

# 2. Read entire file
with open(filename, "r") as f:
    print("\n2. Reading file content:")
    print(f.read())

# 3. Read line by line
with open(filename, "r") as f:
    print("3. Reading file line by line:")
    for line in f:
        print(line, end="")

# 4. Append data
with open(filename, "a") as f:
    f.write("This line is appended\n")
print("\n4. Data appended.")

# 5. Read again after append
with open(filename, "r") as f:
    print("\n5. File after append:")
    print(f.read())


# 7. Delete files
os.remove(new_filename)
os.remove("binary_file.bin")
print("12. Files deleted.")

print("\n---- FILE HANDLING OPERATIONS END ----")

# File Handling
# Types of files: text file and binary file
# operations: open, read and close file

f = open("/Users/ranjeetsinghkushwah/Desktop/pratice intership/demo.txt", "r")

line1 = f.readline()
print(line1)

data = f.read()
print(data)

f.close()

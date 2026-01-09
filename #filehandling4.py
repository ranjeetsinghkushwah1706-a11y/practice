#filehandling4
with open("demo2.txt","w") as f:
    data=f.write("hi everyone\n we are learning file i/o\n using java\n i love programming in java")
    print(data)

with open("demo2.txt","r") as f:
    data=f.read()
    print(data)
new_data=data.replace("java","python")
print(new_data)

with open("demo2.txt","w") as f:
    data=f.write()

#find a word learning

with open("demo2.txt","r") as f:
    data=f.read()
    print(data)
    if(data.find("learning") !=-1):
        print("found")
    else:
        print("not found")    


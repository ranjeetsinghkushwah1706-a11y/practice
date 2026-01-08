#range
#range function returns a sequence of number starting from 0 by default and increament by 
#1 and stop before specific number

#pass is used to make no use of loop

#sum of n natural number 
x=int(input("enter starting range"))
y=int(input("enter ending range"))
count=1
for i in range(x,y):
    count=count+i
print(count)


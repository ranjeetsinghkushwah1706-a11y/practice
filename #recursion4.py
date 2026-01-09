#recursion4
#lenght of list

def length_list(lst,idx=0):
    if(idx==len(lst)):
        return
    print(lst[idx])
    length_list(lst,idx+1)

alpha=["a","b","c","d"]
length_list(alpha)
# Given an array arr of size n which contains elements in range from 0 to n-1, you need to find all the elements occurring more than once in the given array. Return the answer in ascending order. 
# If no such element is found, return list containing [-1].

# Code:

def duplicates(arr):
    dic={}
    new=[]

    #for dictionary manipulations we can use get keyword also ...        
    for i in arr:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
        
    for key in dic.keys():
        if dic[key]>1:
            new.append(key)
    new.sort()
        
    if new==[]:
        return [-1]
    return new

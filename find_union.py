# Question: Given two sorted arrays of size n and m respectively, find their union. 
# The Union of two arrays can be defined as the common and distinct elements in the two arrays. 
# Return the elements in sorted order.

#CODE:

#BruteForce:

def findUnion(arr1,arr2):
        

    seen = set()
    union = set()
    

    for i in arr1:
        seen.add(i)

    for j in arr2:
        seen.add(j)

    for k in seen:
        union.add(k)
    
    return sorted(union) 

#Optimal:
def findUnion(arr1,arr2):
    n=len(arr1)
    m=len(arr2)
    i = 0
    j = 0
    union = []

    while i < n and j < m:
        if arr1[i] < arr2[j]:
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1
        else:
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
            j += 1

    while i < n:
        if len(union) == 0 or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    while j < m:
        if len(union) == 0 or union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    return union
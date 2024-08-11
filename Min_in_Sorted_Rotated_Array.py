# Given a sorted array arr[] (may be distinct or may contain duplicates) of size N that is rotated at some unknown point, 
# the task is to find the minimum element in it.

#CODE:

def findMin(self, arr, n): #O(N)
    m=arr[0]
    
    for i in arr:
        if i<m:
            m=i
    return m 

def findMin(self, arr, n): #O(logN)
    low, high = 0, n - 1
    
    while low < high:
        mid = (low + high) // 2
        
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid
    
    return arr[low]



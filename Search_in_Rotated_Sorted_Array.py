#Question: Given a sorted (in ascending order) and rotated array arr of distinct elements which may be rotated at some point and given an element key, the task is to find the index of the given element key in the array arr. 
# The whole array arr is given as the range to search.
#Rotation shifts elements of the array by a certain number of positions, with elements that fall off one end reappearing at the other end.
#Note:- 0-based indexing is followed & returns -1 if the key is not present.

#CODE:

def search(self,arr,key): #O(N)
    for i in range(len(arr)):
        if arr[i] ==key:
            return i
    return -1

def search(self, arr, key): #O(logN)
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == key:
            return mid
        
        if arr[low] <= arr[mid]:
            if arr[low] <= key < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < key <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    
    return -1

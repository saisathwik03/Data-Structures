#Question: Given an array of strings arr. Return the longest common prefix among each and every strings present in the array. 
# If there's no prefix common in all the strings, return "-1".


#CODE:

def longestCommonPrefix(arr): #O(N*M) N=len(arr), M= len(arr[i])

    prefix = arr[0]
    
    for s in arr[1:]:
        while s[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return -1
    
    return prefix

arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
prefix=longestCommonPrefix(arr)
print("LONGEST PREFIX: ",prefix)
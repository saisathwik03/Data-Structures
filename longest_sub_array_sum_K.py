# Question: Given an array arr containing n integers and an integer k. 
# Your task is to find the length of the longest Sub-Array with the sum of the elements equal to the given value k.

#CODE:

#BRUTEFORCE: O(N^3) && O(N^2)

def lenOfLongSubarr (arr, n, k): #Time limit exceeds
        
    l = 0

    for i in range(n):
        for j in range(i + 1, n + 1):
            s = 0
            
            for K in range(i, j):
                s += arr[K]
            
            if s == k:
                l = max(l, j - i)
                
    return l 


def lenOfLongSubarr (arr, n, k): # Time limit exceeds
    l = 0
    
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += arr[j]
            if s == k:
                l = max(l, j - i + 1)

    return l

# OPTIMAL:

def lenOfLongSubarr (arr, n, k):
    n = len(arr) 
    preSumMap = {}
    Sum = 0
    maxLen = 0
    
    for i in range(n):
        
        Sum += arr[i]


        if Sum == k:
            maxLen = max(maxLen, i + 1)

        rem = Sum - k


        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen = max(maxLen, length)


        if Sum not in preSumMap:
            preSumMap[Sum] = i

    return maxLen
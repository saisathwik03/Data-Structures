# Question: Given an array nums, return true if the array was originally sorted in non-decreasing order, 
# then rotated some number of positions (including zero). Otherwise, return false.
# There may be duplicates in the original array.
# Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

#Code:

def check(nums): #O(n)

    count=0

    for i in range(len(nums)):
        if nums[i] < nums[i-1]:
            count+=1
        
    if count <= 1:
        return True
    else:
        return False


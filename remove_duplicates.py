# Question: Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. 
# Then return the number of unique elements in nums.
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.

#Code:

def removeDuplicates(nums): #O(n^2)

    i=1
    while i<len(nums):
        if nums[i]==nums[i-1]:
            nums.pop(i)
        else:
            i+=1
    return len(nums)

#Optimized Version: Using Two Pointer Method: O(n)

def removeDuplicates(nums):
    if not nums:
        return 0
    
    k = 1 
    
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
    
    return k
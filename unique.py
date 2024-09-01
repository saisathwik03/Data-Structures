# Question: Given a non-empty array of integers nums, every element appears twice except for one. 
# Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# CODE:

def singleNumber(nums):
        
    for i in range(len(nums)):
        if nums.count(nums[i]) == 1:
            return nums[i]

def singleNumber(nums): # bit manipulation
    number = 0

    for i in nums:
        number ^= i
    return number
# Question: Given an array nums containing n distinct numbers in the range [0, n]. 
# Return the only number in the range that is missing from the array.

#CODE:

def missingNumber(nums):
        
    n=len(nums)
    natural = (n*(n+1))//2
    sum_of_nums = sum(nums)
    missing= natural - sum_of_nums
    return missing
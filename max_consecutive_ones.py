# Question: Given a binary array nums, return the maximum number of consecutive 1's in the array.

# CODE:

def findMaxConsecutiveOnes(nums):
        maxi = 0
        result = 0
        
        for num in nums:
            if num == 1:
                result += 1

            else:
                result = 0
            
            if maxi < result:
                maxi = result
        return maxi
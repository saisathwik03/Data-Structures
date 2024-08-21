# Question: Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array. 


#CODE: #O(N)

def moveZeroes(nums):
    print(' intial :',nums)
    count=nums.count(0)
    for _ in range(count):
        nums.remove(0)
    
    print(f'Before: {nums}')

    for _ in range(0,count):
        nums.append(0)
        
    print(f'After: {nums}')
                
    return nums

def moveZeroes(nums):
    last_non_zero = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
            last_non_zero += 1

def moveZeroesToFront(nums):
 
    insert_pos = len(nums) - 1
    
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] != 0:
            nums[insert_pos] = nums[i]
            insert_pos -= 1

    for i in range(insert_pos, -1, -1):
        nums[i] = 0

nums = [0, 1, 0, 3, 12]
moveZeroesToFront(nums)
print(f'Modified: {nums}')

# Question: Given an array nums[], construct a Product Array P (of same size n) 
# such that P[i] is equal to the product of all the elements of nums except nums[i].
# CODE:

def productExceptSelf(self, nums): #Best - O(N)
    n=len(nums)
    p=[0]*n
    left=[1]*n
    right=[1]*n
    
    for i in range(1,n):
        left[i]=left[i-1]*nums[i-1]
    
    for j in range(n-2,-1,-1):
        right[j]=right[j+1]*nums[j+1]
    
    for k in range(n):
        p[k]=left[k]*right[k]
    return p
#Question: Given an array arr, return the second largest distinct element from an array. If the second largest element doesn't exist then return -1.

#Code:

def print2largest(arr):
        # Code Here
        
        max1=-1
        max2=-1
        
        for i in arr:
            if i>max1:
                max2=max1
                max1=i
            elif i>max2 and max1!=i:
                max2=i
        return max2

#Time complexity of above code is O(n)
# Question: Given an array arr[] that contains n integers (may be positive, negative or zero). 
# Find the product of the maximum product subarray.

#Code:

#Optimized Version: O(n) - Best

def maxProduct(arr, n):

    max_so_far = arr[0]
    min_so_far = arr[0]
    result = arr[0]

    for i in range(1, n):
        current = arr[i]
        temp_max = max(current, max_so_far * current, min_so_far * current)
        min_so_far = min(current, max_so_far * current, min_so_far * current)
        max_so_far = temp_max

        if max_so_far > result:
            result = max_so_far

    return result

#Brute Force : O(n^2) - Worse

def maxProductBruteForce(arr, n):
    max_product = float('-inf')

    for i in range(n):
        current_product = 1
        for j in range(i, n):
            current_product *= arr[j]
            if current_product > max_product:
                max_product = current_product

    return max_product

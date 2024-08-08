# Question: Given an integer array arr[]. Find the contiguous sub-array(containing at least one number) that has the maximum sum and return its sum.

#CODE:

#USing Kadane's Algorithm : O(n) - Best case

def maxSubArraySum(arr):
    size = len(arr)
    max_so_far = float('-inf')
    max_ending_here = 0
    start = end = s = 0

    for i in range(size):
        max_ending_here += arr[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1

    print(f"Maximum sum: {max_so_far}")
    print(f"Sub-array: {arr[start:end + 1]}")
    return max_so_far


# Brute Force Approach: O(n^2) - Worst Case

def maxSubArraySumBruteForce(arr):
    size = len(arr)
    max_sum = float('-inf')
    start = end = 0

    for i in range(size):
        current_sum = 0
        for j in range(i, size):
            current_sum += arr[j]
            if current_sum > max_sum:
                max_sum = current_sum
                start = i
                end = j

    print(f"Maximum sum: {max_sum}")
    print(f"Sub-array: {arr[start:end + 1]}")
    return max_sum

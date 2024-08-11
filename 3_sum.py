#Question: Given an array arr[] of n integers. Check whether it contains a triplet that sums up to zero. 
# Return true, if there is at least one triplet following the condition else return false.

#CODE:

#O(N^2) - 2 codes - Best Possible Versions

def findTriplets(self, arr, n):
    arr.sort()
    
    for i in range(n):
        seen = set()
        current_sum = 0 - arr[i]
        
        for j in range(i + 1, n):
            if current_sum - arr[j] in seen:
                return 1
            seen.add(arr[j])
    
    return 0

def findTriplets(self, arr, n):
    arr.sort()
    
    for i in range(n - 2):
        left, right = i + 1, n - 1
        
        while left < right:
            total = arr[i] + arr[left] + arr[right]
            
            if total == 0:
                return 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return 0

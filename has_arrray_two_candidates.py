# Question: Given an array arr of positive integers and another number x. Determine whether two elements exist in arr whose sum is exactly x or not. 
# Return a boolean value true if two elements exist in arr else return false.

#Code:

# Worst Case - O(n^2)
def hasArrayTwoCandidates(arr, x):
	
	for i in range(0,len(arr)-1):
		for j in range(i+1,len(arr)):
			if arr[i]+arr[j] == x:
				return 1
	return 0

# Average Case - using Two pointer method - O(n)

def hasArrayTwoCandidates(arr, x):

	arr.sort()
	size=len(arr)
	i=0
	j=size-1
	while i<j:
		sum_of=arr[i]+arr[j]
		if sum_of == x:
			return 1
		elif sum_of>x:
			j-=1
		else:
			i+=1
	return 0

#Best Case - using set operations - O(1)

def hasArrayTwoCandidates(arr, x):
    seen = set()
    for num in arr:
        if (x - num) in seen:
            return True
        seen.add(num)
    return False

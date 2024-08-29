# Question: Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.

# CODE: O(N^2)/ O(N)

def countSubstrings(s): 
        count = 0 

        for i in range(len(s)):

            count += countPalindrome(s,i, i)
            count += countPalindrome(s, i, i+1)

        return count
            
            
def countPalindrome(s, left, right): #Helper Function
    count = 0 

    while left >= 0 and right < len(s) and s[left] == s[right]:
        count += 1
        left -= 1
        right += 1

    return count

s='aaa'
count = countSubstrings(s)
print(f'Count: {count}')

# Manacher’s Algorithm

def countSubstrings(s): #O(N)
    # Step 1: Transform the string with special characters manually
    n = len(s)
    t = [''] * (2 * n + 3)
    t[0] = '^'
    t[-1] = '$'
    
    index = 1
    for i in range(n):
        t[index] = '#'
        t[index + 1] = s[i]
        index += 2
    t[index] = '#'

    # Step 2: Initialize variables
    P = [0] * len(t)
    center = right = 0
    
    # Step 3: Process the transformed string
    for i in range(1, len(t) - 1):
        if i < right:
            P[i] = min(right - i, P[2 * center - i])
        
        # Expand around center i
        while t[i + P[i] + 1] == t[i - P[i] - 1]:
            P[i] += 1
        
        # Update the center and right boundary
        if i + P[i] > right:
            center, right = i, i + P[i]
    
    # Step 4: Calculate the number of palindromic substrings
    return sum((v + 1) // 2 for v in P)

s = 'aaa'
count = countSubstrings(s)
print(f'Count: {count}')


# Question: Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.

# CODE:

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
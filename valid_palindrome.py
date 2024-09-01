# Question: A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

#CODE:

def isPalindrome(s):
    dup=''
    for i in s:
        if i.isalnum():
            dup+=i
    
    print(dup)
    if dup.lower() == dup[::-1].lower():
        return True
    return False

s="A man, a plan, a canal: Panama"
print(isPalindrome(s))
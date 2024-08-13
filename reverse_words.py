#Question: Given a String S, reverse the string without reversing its individual words. 
# Words are separated by dots.

#CODE: O(N)

def reverseWords(S):
    
    s=S.split('.')
    rev=''
    i=len(s)-1
    while i>=0:
        rev+=s[i]+'.'
        i-=1
    return rev[0:i:1]

def reverseWords(S):
    s = S.split('.')
    rev = s[-1]
    for i in range(len(s) - 2, -1, -1):
        rev += '.' + s[i]
    return rev
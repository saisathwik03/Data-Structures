# Question: Given a string s, the objective is to convert it into integer format without utilizing any built-in functions. 
# If the conversion is not feasible, the function should return -1.

# Note: Conversion is feasible only if all characters in the string are numeric 
# or if its first character is '-' and rest are numeric.

#CODE:

def atoi(s): #O(N)
    
    if s[0] == '-':
        s = s[1:]
        negative = True
    else:
        negative = False
    
    if not s.isdigit():
        return -1
    
    num = 0
    for char in s:
        num = num * 10 + int(char)
    
    if negative:
        return -num
    else:
        return num
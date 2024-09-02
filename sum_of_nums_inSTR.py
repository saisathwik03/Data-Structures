# QUESTION: Given a string str containing alphanumeric characters. 
# The task is to calculate the sum of all the numbers present in the string.
"""""
Example 1:

Input:
str = 1abc23
Output: 24
Explanation: 1 and 23 are numbers in the
string which is added to get the sum as
24.
"""""

# CODE:

def findSum(s):
        
    numStr = ''
    total = 0
    
    for char in s:
        
        if char.isdigit():
            numStr+=char
        
        else:
            if numStr:
                total+=int(numStr)
                numStr=''
    
    if numStr:
        total += int(numStr)
    
    return total

# Optimal:

def findSum(s):
    import re
    numbers = re.findall(r'\d+', s)
    integers = map(int, numbers)
    total = sum(integers)
    return total

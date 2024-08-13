# Question: Given a string in roman no format (s)  your task is to convert it to an integer.
# Various symbols and their values are given below.
"""
I 1
V 5
X 10
L 50
C 100
D 500
M 1000
"""

#CODE:

def romanToDecimal(S): #O(N): Best Case
    di = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    
    ans = 0
    prev_value = 0
    
    for roman in S[::-1]:  
        int_value = di[roman]
        if int_value < prev_value:
            ans -= int_value
        else:
            ans += int_value
        prev_value = int_value
    
    return ans

# roman = 'IX'
# integer = romanToDecimal(roman)
# print('Integer: ', integer)

def romanToDecimalBruteForce(S): #O(N^2) : Worst Case
    di = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    ans = 0
    i = 0
    
    while i < len(S):
        if i + 1 < len(S) and di[S[i]] < di[S[i + 1]]:
            ans += di[S[i + 1]] - di[S[i]]
            i += 2
        else:
            ans += di[S[i]]
            i += 1
    
    return ans

# roman = 'IX'
# integer = romanToDecimal(roman)
# print('Integer: ', integer)

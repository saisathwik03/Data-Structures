# Question : You are given a string num, representing a large integer. 
# Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.
# A substring is a contiguous sequence of characters within a string.

# CODE:

#Using kadane's Algo
def largestOddNumber(num):

    lar_odd_num = ""
    current = ""
    
    for i in num:
        current += i
        if int(i) % 2 != 0:
            lar_odd_num = current
    
    return lar_odd_num  

def largestOddNumber(num):

        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[:i+1]
        return "" 
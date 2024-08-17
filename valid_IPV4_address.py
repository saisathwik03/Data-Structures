# Question: You are given a string str in the form of an IPv4 Address. 
# Your task is to validate an IPv4 Address, if it is valid return true otherwise return false.
# IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, 
# separated by dots, e.g., 172.16.254.1
# A valid IPv4 Address is of the form x1.x2.x3.x4 where 0 <= (x1, x2, x3, x4) <= 255. 
# Thus, we can write the generalized form of an IPv4 address as (0-255).(0-255).(0-255).(0-255)
# Note: Here we are considering numbers only from 0 to 255 and any additional leading zeroes will be considered invalid.


#CODE: O(N)

def isValid(s):
    l = s.split('.')
    l2 = []

    if len(l) != 4:
        return False

    for i in l:
        if i.isdigit() and (len(i) == 1 or i[0] != '0'):
            l2.append(int(i))
        else:
            return False

    size = len(l2)
    if s.count('.') == size - 1:
        for i in range(len(l2)):
            if not (0 <= l2[i] <= 255):
                return False
        return True
    return False

def isValid(s):
    parts = s.split('.')
    
    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit() or (len(part) > 1 and part[0] == '0') or not (0 <= int(part) <= 255):
            return False

    return True
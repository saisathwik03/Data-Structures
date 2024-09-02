# Question: Given a string str, convert the first letter of each word in the string to uppercase. 

#CODE:

def transform(s):
    l = s.split(' ')
    new = ''
    
    for i in range(len(l)):
        l[i] = l[i][0].upper() + l[i][1:]
    
    for word in l:
        new += word + ' '
    
    return new.strip()

def transform(s):
    l = s.split(' ')
    new = ''
    
    for word in l:
        new += word[0].upper() + word[1:] + ' '
    
    return new.strip()

print(transform("i love programming"))

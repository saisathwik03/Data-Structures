# Question: Given a string S on which you need to perform Q replace operations.
# Each replacement operation has 3 parameters: a starting index i, a source word x and a target word y. 
# The rule is that if x starts at position i in the original string S, then we will replace that occurrence of x with y. 
# If not, we do nothing.
# Note: All these operations occur simultaneously. It's guaranteed that there won't be any overlap in replacement: for example, S = "abc", indexes = [0,1], sources = ["ab", "bc"] is not a valid test case.

#CODE:

def findAndReplace(S, Q, index, sources, targets):
    print(f'S: {S}, Q: {Q}, index: {index}, sources: {sources}, targets: {targets}')
    size=len(S)
    for i in range(size):
        if (S[i] in  sources) and (i in index):
            S.replace(S[i],targets[i])
    return S



S = "gforks" # Original and given string
Q = 2 #no of replace operations
index = [0, 4] # indexes to replace
sources = ["g", "ks"] # to replace the words using indexes
targets = ["geeks", "geeks"] 

replaced=findAndReplace(S,Q,index,sources,targets)
print('Replaced: ', replaced)
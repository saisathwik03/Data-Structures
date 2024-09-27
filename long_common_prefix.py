# Question: Write a function to find the longest common prefix string 
# amongst an array of strings. If there is no common prefix, return an empty string "".

#CODE:

def longestCommonPrefix(strs):
    if not strs:
        return ""

    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return strs[0][:i]

    return strs[0]
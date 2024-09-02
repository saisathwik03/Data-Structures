# CODE:

def checkRedundancy(self, s):
    
    stack = []
    matching_braces = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            top = stack.pop()
            found_operator = False

            while top != matching_braces[char]:
                if top in '+-*/':
                    found_operator = True
                top = stack.pop()

            if not found_operator:
                return 1

    return 0
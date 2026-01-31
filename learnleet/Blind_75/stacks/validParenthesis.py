


def is_valid(s):
    stack = []
    mapping = {
        ')':'(',
        '}': '{',
        ']':'['
    }

    for char in s:
        if char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False    
            stack.pop()
        else:
            stack.append(char)

    return len(stack) == 0
































def valid_paren(s):

    stack = []
    paren_list = {')':'(', '}':'{',']':'['}

    for char in s:
        if not stack or stack[-1] != paren_list[char]:
            return False
            stack.pop()
        
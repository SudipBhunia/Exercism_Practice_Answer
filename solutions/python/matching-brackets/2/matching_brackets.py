PAIR = {
    ')': '(',
    ']': '[',
    '}': '{'
}

def is_paired(input_string):
    stack = []

    for char in input_string:
        if char in '([{':  # Opening bracket
            stack.append(char)
        elif char in ')]}':  # Closing bracket
            if not stack or stack[-1] != PAIR[char]:
                return False
            stack.pop()
    return not stack

 # Define operations
operations = {
    "plus": lambda x, y: x + y,
    "minus": lambda x, y: x - y,
    "multiplied": lambda x, y: x * y,
    "divided": lambda x, y: x // y
}

 # Helper function to check if token is a number
def is_number(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def answer(question):
    # Validate and extract expression
    question = question.strip().lower()
    if not question.startswith('what is ') or not question.endswith('?'):
        raise ValueError("syntax error")

    question = question[:-1].removeprefix('what is ').strip()
    if not question:
        raise ValueError("syntax error")

    # Normalize "multiplied by" and "divided by" to single tokens
    question = question.replace("multiplied by", "multiplied")
    question = question.replace("divided by", "divided")

    tokens = question.split()

    # Validate structure: must alternate number, operation, number, operation...
    if not is_number(tokens[0]):
        raise ValueError("syntax error")

    # Check for valid alternating pattern
    for i, token in enumerate(tokens):
        if i % 2 == 0:
            if not is_number(token):
                raise ValueError("syntax error")
        else:
            if is_number(token):
                raise ValueError("syntax error")
            if token not in operations:
                raise ValueError("unknown operation")

    # Must end with a number (even index count)
    if len(tokens) % 2 == 0:
        raise ValueError("syntax error")

    # Evaluate left to right
    result = int(tokens[0])
    for i in range(1, len(tokens), 2):
        operation = tokens[i]
        operand = int(tokens[i+1])
        result = operations[operation](result, operand)

    return result
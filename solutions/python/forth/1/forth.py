class StackUnderflowError(Exception):
    def __init__(self, message):
        super().__init__(message)


def evaluate(input_data):
    stack = []
    definitions = {}

    tokens = []
    for line in input_data:
        tokens.extend(line.lower().split())

    i = 0

    while i < len(tokens):
        token = tokens[i]

        # ------------------------
        # Definition
        # ------------------------
        if token == ":":
            if i + 1 >= len(tokens):
                raise ValueError("invalid definition")

            word_name = tokens[i + 1]

            if word_name.lstrip("-").isdigit():
                raise ValueError("illegal operation")

            i += 2
            definition = []

            while i < len(tokens) and tokens[i] != ";":
                t = tokens[i]

                # EARLY BINDING HERE
                if t in definitions:
                    definition.extend(definitions[t])
                else:
                    definition.append(t)

                i += 1

            if i >= len(tokens):
                raise ValueError("invalid definition")

            definitions[word_name] = definition
            i += 1
            continue

        # ------------------------
        # User-defined words
        # ------------------------
        if token in definitions:
            # Inject expanded definition into tokens
            tokens = tokens[:i] + definitions[token] + tokens[i+1:]
            continue

        # ------------------------
        # Numbers
        # ------------------------
        if token.lstrip("-").isdigit():
            stack.append(int(token))

        # ------------------------
        # Arithmetic
        # ------------------------
        elif token == "+":
            if len(stack) < 2:
                raise StackUnderflowError("Insufficient number of items in stack")
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)

        elif token == "-":
            if len(stack) < 2:
                raise StackUnderflowError("Insufficient number of items in stack")
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)

        elif token == "*":
            if len(stack) < 2:
                raise StackUnderflowError("Insufficient number of items in stack")
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)

        elif token == "/":
            if len(stack) < 2:
                raise StackUnderflowError("Insufficient number of items in stack")
            b = stack.pop()
            a = stack.pop()
            if b == 0:
                raise ZeroDivisionError("divide by zero")
            stack.append(a // b)

        # ------------------------
        # Stack operations
        # ------------------------
        elif token == "dup":
            if len(stack) < 1:
                raise StackUnderflowError("Insufficient number of items in stack")
            stack.append(stack[-1])

        elif token == "drop":
            if len(stack) < 1:
                raise StackUnderflowError("Insufficient number of items in stack")
            stack.pop()

        elif token == "swap":
            if len(stack) < 2:
                raise StackUnderflowError("Insufficient number of items in stack")
            stack[-1], stack[-2] = stack[-2], stack[-1]

        elif token == "over":
            if len(stack) < 2:
                raise StackUnderflowError("Insufficient number of items in stack")
            stack.append(stack[-2])

        else:
            raise ValueError("undefined operation")

        i += 1

    return stack
EQ = ['plus', 'minus', 'multiplied', 'divided']
def is_number(num):
    try:
        int(num)
        return True
    except ValueError:
        return False
def answer(question):
    question = question.strip().lower()
    if not question.startswith('what is ') or not question.endswith('?'):
        raise ValueError("syntax error")

    question = question.removeprefix("what is")
    question = question.removesuffix("?")
    question = question.replace("by", "")
    question = question.strip()

    if not question:
        raise ValueError("syntax error")
    tokens = question.split()
    for i, token in enumerate(tokens):
        if i % 2 == 0:
            if not is_number(token):
                raise ValueError("syntax error")
        else:
            if is_number(token):
                raise ValueError("syntax error")
            if token not in EQ:
                raise ValueError("unknown operation")
    while len(tokens) > 1:
            try:
                x_value = int(tokens[0])
                y_value = int(tokens[2])
                symbol = tokens[1]
                remainder = tokens[3:]

                if symbol == "plus":
                    tokens = [x_value + y_value] + remainder
                elif symbol == "minus":
                    tokens = [x_value - y_value] + remainder
                elif symbol == "multiplied":
                    tokens = [x_value * y_value] + remainder
                elif symbol == "divided":
                    tokens = [x_value / y_value] + remainder
                else:
                    raise ValueError("syntax error")
            except:
                raise ValueError("syntax error")
    return int(tokens[0])
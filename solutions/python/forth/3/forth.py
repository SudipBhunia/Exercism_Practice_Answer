class StackUnderflowError(Exception):
    def __init__(self, message):
        self.message = message

def evaluate(input_data):
    stack = []
    keywords = {}

    def isnum(line):
        return line.isdigit() or line.startswith('-') and line[1:].isdigit()
    
    def run(commands):
        for elem in commands:
            if elem in keywords:
                run(keywords[elem].split())
            else:
                try:
                    if isnum(elem):
                        stack.append(int(elem))
                    elif elem in '+*':
                        stack.append(stack.pop() + stack.pop() if elem == '+' else stack.pop() * stack.pop())
                    elif elem in '-/':
                        tmp = stack.pop()
                        stack.append(stack.pop() - tmp if elem == '-' else stack.pop() // tmp)
                    elif elem == 'dup':
                        stack.append(stack[-1])
                    elif elem == 'drop':
                        stack.pop()
                    elif elem == 'swap':
                        stack[-1], stack[-2] = stack[-2], stack[-1]
                    elif elem == 'over':
                        stack.append(stack[-2])
                    else:
                        raise ValueError('undefined operation')
                except KeyError:
                    raise ValueError('undefined operation')
                except IndexError:
                    raise StackUnderflowError('Insufficient number of items in stack')
                except ZeroDivisionError:
                    raise ZeroDivisionError('divide by zero')
                
    for data in input_data:
        if data.startswith(': ') and data.endswith(' ;'):
            data = data[2:-2].lower().split(' ', 1)
            if len(data) < 2 or isnum(data[0]):
                raise ValueError('illegal operation')
            keywords[data[0]] = ' '.join(keywords.get(item, item) for item in data[1].split())
        else:
            run(data.lower().split())

    return stack

 
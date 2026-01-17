CODE = ['wink', 'double blink', 'close your eyes', 'jump']
def commands(binary_str):
    binary_str = list(binary_str)
    binary_str.reverse()
    temp = []
    for i in range(len(binary_str) - 1):
        if bool(int(binary_str[i])) == True:
            temp.append(CODE[i])
    if bool(int(binary_str[-1])) == True:
        temp.reverse()
    return temp
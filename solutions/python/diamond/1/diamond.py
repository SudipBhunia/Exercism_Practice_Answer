def rows(letter):
    val = (ord(letter) - ord('A')) * 2 + 1
    temp = ord('A')
    index = [val // 2, val // 2]
    text = ''
    li = []
    for i in range(val // 2 + 1):
        for j in range(val):
            if j in index:
                # print(chr(temp), end='')
                text += chr(temp)
            else:
                # print(' ', end='')
                text += ' '
        temp += 1
        index = [index[0] - 1, index[1] + 1]
        # print()
        text += '.'

    temp -= 2
    index = [1, val - 2]
    for i in range(val // 2,0, -1):
        for j in range(val):
            if j in index:
                # print(chr(temp), end='')
                text += chr(temp)
            else:
                # print(' ', end='')
                text += ' '
        temp -= 1
        index = [index[0] + 1, index[1] - 1]
        # print()
        text += '.'
    return text.split('.')[:-1]
def rotate(text, key):
    li = list(text)
    for i in range(len(li)):
        if li[i].isalpha():
            val = ord(li[i]) + key
            if li[i].isupper():
                if val > ord('Z'):
                    val = val - 26
                    li[i] = chr(val)
                else:
                    li[i] = chr(val)
            elif li[i].islower():
                if val > ord('z'):
                    val = val - 26
                    li[i] = chr(val)
                else:
                    li[i] = chr(val)
    return ''.join(li)
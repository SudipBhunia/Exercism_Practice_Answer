def rotate(text, key):
    li = list(text)
    for i in range(len(li)):
        if li[i].isalpha():
            if li[i].isupper():
                li[i] = chr((ord(li[i]) - 65 + key) % 26 + 65)
            elif li[i].islower():
                li[i] = chr((ord(li[i]) - 97 + key) % 26 + 97)
    return ''.join(li)
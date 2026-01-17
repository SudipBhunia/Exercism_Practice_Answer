def is_valid(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
    # li = [int(item) for item in isbn if item.isdecimal()]
    val = 0
    for i in range(len(isbn) - 1):
        if isbn[i].isdecimal():
            val = val + (int(isbn[i]) * (len(isbn) - i))
        else:
            return False
    if isbn[-1].isalpha():
        if isbn.endswith('X'):
            val = val + 10
            return val % 11 == 0
        else:
            return False
    return (val + int(isbn[-1])) % 11 == 0
FROM_CHARS = 'abcdefghijklmnopqrstuvwxyz,. '
TO_CHARS = 'zyxwvutsrqponmlkjihgfedcba   '
def encode(plain_text):
    result = plain_text.lower().translate(str.maketrans(FROM_CHARS, TO_CHARS)).replace(' ', '')
    if len(result) > 5:
        res = ''
        for i in range(0, len(result), 5):
            res += result[i:i + 5] + ' '
        return res.strip()
    return result.strip()

def decode(plain_text):
    return plain_text.lower().translate(str.maketrans(FROM_CHARS, TO_CHARS)).replace(' ', '').strip()
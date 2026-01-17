def is_pangram(sentence):
    total = 0
    for text in set(sentence.upper()):
        if text.isalpha():
            total += ord(text)
    if total == 2015:
        return True
    return False

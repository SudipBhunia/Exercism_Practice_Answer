def is_isogram(string):
    li = [item.lower() for item in string if item.isalpha()]
    return len(li) == len(set(li))

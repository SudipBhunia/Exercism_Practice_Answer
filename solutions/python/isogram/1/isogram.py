def is_isogram(string):
    string = string.replace(' ', '').replace('-','').lower()
    return sorted(string) == sorted(set(string.lower()))

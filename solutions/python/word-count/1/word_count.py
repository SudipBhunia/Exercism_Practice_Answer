def count_words(sentence):
    from collections import Counter
    import re
    words = re.findall(r"[a-z0-9]+(?:'[a-z]+)?", sentence.lower())
    return dict(Counter(words))
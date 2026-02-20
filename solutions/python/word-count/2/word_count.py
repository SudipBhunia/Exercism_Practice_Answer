from collections import Counter
import re
def count_words(sentence):
    words = re.findall(r"[a-z0-9]+(?:'[a-z]+)?", sentence.lower())
    return dict(Counter(words))
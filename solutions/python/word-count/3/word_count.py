from collections import Counter
import re
import sys
def count_words(sentence):
    words = re.findall(r"[a-z0-9]+(?:'[a-z]+)?", sentence.lower())
    return dict(Counter(words))
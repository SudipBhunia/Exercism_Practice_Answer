def find_anagrams(word, candidates):
    return [ch for ch in candidates if len(word) == len(ch) and sorted(word.lower()) == sorted(ch.lower()) and word.lower() != ch.lower()]
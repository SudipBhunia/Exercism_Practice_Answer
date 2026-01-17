def find_anagrams(word, candidates):
    return [
            ch
            for ch in candidates
            if sorted(word.casefold()) == sorted(ch.casefold()) 
            and word.casefold() != ch.casefold()
            ]
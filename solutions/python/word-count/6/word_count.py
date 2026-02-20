def count_words(sentence):
    import string
    
    # Create translation table: keep alphanumeric and apostrophes, replace others with space
    translator = str.maketrans({c: ' ' for c in string.punctuation if c != "'"})
    sentence = sentence.lower().translate(translator)
    
    words = [word.strip("'") for word in sentence.split() if word.strip("'")]
    
    return {word: words.count(word) for word in set(words)}
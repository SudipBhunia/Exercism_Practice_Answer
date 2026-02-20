def count_words(sentence):
    sentence = sentence.lower()
    
    # Replace non-alphanumeric chars (except space and ') with space
    for char in sentence:
        if not (char.isalnum() or char in [' ', "'"]):
            sentence = sentence.replace(char, ' ')
    
    words = [word.strip("'") for word in sentence.split() if word.strip("'")]
    
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts
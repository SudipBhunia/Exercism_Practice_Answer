def recite(start_verse, end_verse):
    animals = [
        ("fly", None),
        ("spider", "It wriggled and jiggled and tickled inside her."),
        ("bird", "How absurd to swallow a bird!"),
        ("cat", "Imagine that, to swallow a cat!"),
        ("dog", "What a hog, to swallow a dog!"),
        ("goat", "Just opened her throat and swallowed a goat!"),
        ("cow", "I don't know how she swallowed a cow!"),
        ("horse", "She's dead, of course!")
    ]
    
    verses = []
    
    for verse_num in range(start_verse - 1, end_verse):
        animal, comment = animals[verse_num]
        verse_lines = []
        
        verse_lines.append(f"I know an old lady who swallowed a {animal}.")
        
        if animal == "horse":
            verse_lines.append(comment)
        else:
            if comment:
                verse_lines.append(comment)
            
            for i in range(verse_num, 0, -1):
                prev_animal = animals[i][0]
                prev_prev_animal = animals[i - 1][0]
                
                if prev_prev_animal == "spider":
                    verse_lines.append(
                        f"She swallowed the {prev_animal} to catch the {prev_prev_animal} "
                        f"that wriggled and jiggled and tickled inside her."
                    )
                else:
                    verse_lines.append(
                        f"She swallowed the {prev_animal} to catch the {prev_prev_animal}."
                    )
            
            verse_lines.append("I don't know why she swallowed the fly. Perhaps she'll die.")
        
        verses.extend(verse_lines)
        if verse_num < end_verse - 1:
            verses.append("")
    
    return verses

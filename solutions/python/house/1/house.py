def recite(start_verse, end_verse):
    parts = [
        "the house that Jack built",
        "the malt that lay in",
        "the rat that ate",
        "the cat that killed",
        "the dog that worried",
        "the cow with the crumpled horn that tossed",
        "the maiden all forlorn that milked",
        "the man all tattered and torn that kissed",
        "the priest all shaven and shorn that married",
        "the rooster that crowed in the morn that woke",
        "the farmer sowing his corn that kept",
        "the horse and the hound and the horn that belonged to",
    ]

    verses = []

    for verse_num in range(start_verse, end_verse + 1):
        # Build the verse by joining parts from verse_num down to 1
        verse_parts = ["This is"]

        for i in range(verse_num - 1, -1, -1):
            verse_parts.append(parts[i])

        # Join all parts and add period
        verse = " ".join(verse_parts) + "."
        verses.append(verse)

    return verses

def recite(start_verse, end_verse):
    days = [
        "first", "second", "third", "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
    ]
    
    gifts = [
        "a Partridge in a Pear Tree",
        "two Turtle Doves",
        "three French Hens",
        "four Calling Birds",
        "five Gold Rings",
        "six Geese-a-Laying",
        "seven Swans-a-Swimming",
        "eight Maids-a-Milking",
        "nine Ladies Dancing",
        "ten Lords-a-Leaping",
        "eleven Pipers Piping",
        "twelve Drummers Drumming"
    ]
    
    verses = []
    
    for verse_num in range(start_verse, end_verse + 1):
        day = days[verse_num - 1]
        verse = f"On the {day} day of Christmas my true love gave to me: "
        
        gifts_list = []
        for i in range(verse_num - 1, -1, -1):
            if i == 0 and verse_num > 1:
                gifts_list.append(f"and {gifts[i]}")
            else:
                gifts_list.append(gifts[i])
        
        verse += ", ".join(gifts_list) + "."
        verses.append(verse)
    
    return verses
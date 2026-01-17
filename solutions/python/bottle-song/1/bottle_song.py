def recite(start, take = 1):
    verses = []
    
    for num in range(start, start - take, -1):
        verse = generate_verse(num)
        verses.extend(verse)
        
        # Add empty string between verses (except after the last one)
        if num > start - take + 1:
            verses.append("")
    
    return verses

def generate_verse(num):
    if num == 0:
        return []
    
    # Convert number to word
    current = number_to_word(num)
    next_num = number_to_word(num - 1)
    
    # Capitalize first letter of verse
    current_cap = current.capitalize()
    
    # Handle plural/singular
    bottle_current = "bottle" if num == 1 else "bottles"
    bottle_next = "bottle" if num - 1 == 1 else "bottles"
    
    line1 = f"{current_cap} green {bottle_current} hanging on the wall,"
    line2 = f"{current_cap} green {bottle_current} hanging on the wall,"
    line3 = f"And if one green bottle should accidentally fall,"
    line4 = f"There'll be {next_num} green {bottle_next} hanging on the wall."
    
    return [line1, line2, line3, line4]

def number_to_word(num):
    numbers = {
        0: "no", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"
    }
    return numbers.get(num, str(num))
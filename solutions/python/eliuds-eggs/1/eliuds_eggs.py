def egg_count(display_value):
    binary = bin(display_value).removeprefix('0b')
    count = 0
    for digit in binary:
        count += int(digit)
    return count
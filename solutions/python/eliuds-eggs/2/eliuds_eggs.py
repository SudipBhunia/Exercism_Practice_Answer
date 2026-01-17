def egg_count(display_value):
    return sum(map(int, list(bin(display_value).removeprefix('0b'))))
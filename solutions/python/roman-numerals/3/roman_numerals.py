def roman(number):
    assert (number > 0)

    # define lookup table (as a tuple of tuples, in this case)
    table = (
        ("I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"),
        ("X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"),
        ("C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"),
        ("M", "MM", "MMM"))

    # convert the input integer to a list of single digits
    digits = [int(d) for d in str(number)]
    
    # we need the row in the lookup table for our most-significant decimal digit
    inverter = len(digits) - 1 

    # translate decimal digits list to Roman numerals list
    roman_digits = [table[inverter - i][d - 1] for (i, d) in enumerate(digits) if d != 0]

    # convert the list of Roman numerals to a single string
    return ''.join(roman_digits)
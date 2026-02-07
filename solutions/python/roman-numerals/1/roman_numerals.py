def roman(number):
    if number < 1 or number > 3999:
        raise ValueError("Number must be between 1 and 3999")
    
    values = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]
    
    result = ""
    
    for value, numeral in values:
        count = number // value
        if count:
            result += numeral * count
            number -= value * count
    
    return result

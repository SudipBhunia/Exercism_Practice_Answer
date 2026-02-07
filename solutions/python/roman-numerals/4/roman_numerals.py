
def roman(number):
    if not 1 <= number <= 3999:
        raise ValueError("Number must be between 1 and 3999")
    
    mapping = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    result = []
    for value, numeral in mapping:
        count, number = divmod(number, value)
        result.append(numeral * count)
    
    return ''.join(result)

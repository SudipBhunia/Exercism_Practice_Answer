def is_armstrong_number(number):
    length = len(str(number))
    result = 0
    for item in str(number):
        result += int(item) ** length
    return number == result

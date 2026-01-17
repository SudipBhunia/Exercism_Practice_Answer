def is_armstrong_number(number):
    return number == sum([int(item) ** len(str(number)) for item in str(number)])

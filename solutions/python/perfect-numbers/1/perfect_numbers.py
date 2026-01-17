def aliquot(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum

def classify(number):
    if number < 1: raise ValueError("Classification is only possible for positive integers.")
    if aliquot(number) == number: return 'perfect'
    if aliquot(number) > number: return 'abundant'
    if aliquot(number) < number: return 'deficient'

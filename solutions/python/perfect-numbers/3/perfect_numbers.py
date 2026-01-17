def classify(number):
    if number < 1: raise ValueError("Classification is only possible for positive integers.")
    aliquot = sum(i for i in range(1,number // 2 +1) if not number % i)
    if aliquot == number: return 'perfect'
    if aliquot > number: return 'abundant'
    return 'deficient'

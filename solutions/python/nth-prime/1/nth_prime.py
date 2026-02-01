import math
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i) == 0:
            return False
    return True
def prime(number):
    count = 0
    num = 1
    if number <= 0:
        raise ValueError('there is no zeroth prime')
    while count != number:
        num += 1
        if is_prime(num):
            count += 1
    return num

def prime_range(limit):
    prime_array = []
    for i in range(1, limit + 1):
        prime_array.append(prime(i))
    return prime_array
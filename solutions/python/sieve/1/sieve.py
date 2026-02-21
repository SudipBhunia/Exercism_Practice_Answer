import math
def check_prime(num):
    flag = True
    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            flag = False
            break
    return flag
def primes(limit):
    return [num for num in range(2, limit + 1) if check_prime(num)]
'''
Creating functions to check whether is a number is prime or not and 
how many prime numbers are there to the limit.
'''
import math
def check_prime(num):
    return all(num % check for check in range(2, int(math.sqrt(num)) + 1))
def primes(limit):
    return [num for num in range(2, limit + 1) if check_prime(num)]
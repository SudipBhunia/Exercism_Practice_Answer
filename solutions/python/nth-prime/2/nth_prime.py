def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
    counter = 2
    primes = [2]
    while len(primes) < number: 
        counter += 1
        if all(counter % test != 0 for test in primes):
            primes.append(counter)
    return primes[-1]
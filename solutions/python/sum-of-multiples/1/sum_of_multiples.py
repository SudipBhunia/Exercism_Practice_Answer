def sum_of_multiples(limit, multiples):
    li = [i for i in range(limit) for j in multiples if j != 0 and i % j == 0]
    return sum(set(li))
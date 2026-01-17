def square_root(number):
    L = 0
    R = number + 1
    
    while (L != R - 1):
        M = (L + R) // 2
        if (M * M <= number):
            L = M
        else:
            R = M
    return L
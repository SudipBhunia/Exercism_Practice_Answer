from math import sqrt
def score(x, y):
    val = sqrt(x*x + y*y)
    if 5 < val <= 10: return 1
    if 1 < val <= 5: return 5
    if 0 <= val <= 1: return 10
    return 0

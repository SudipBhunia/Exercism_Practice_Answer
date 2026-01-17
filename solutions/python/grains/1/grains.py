def square(number):
    if 1 > number or number > 64:
        raise ValueError("square must be between 1 and 64")
    res = 1
    for i in range(2,number + 1):
        res = res * 2
    return res
    

def total():
    temp = 0
    for i in range(1, 65):
        temp += square(i)
    return temp
    

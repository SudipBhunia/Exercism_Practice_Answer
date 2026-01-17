def div_3(number):
    return number % 3 == 0
def div_5(number):
    return number % 5 == 0
def div_7(number):
    return number % 7 == 0

def convert(number):
    text = ''
    if div_3(number):
        text = text + 'Pling'
        if div_5(number):
            text = text + 'Plang'
            if div_7(number):
                text = text + 'Plong'
        elif div_7(number):
            text = text + 'Plong'
    elif div_5(number):
        text = text + 'Plang'
        if div_7(number):
            text = text + 'Plong'
    elif div_7(number):
        text = text + 'Plong'
    else:
        text = str(number)
    return text

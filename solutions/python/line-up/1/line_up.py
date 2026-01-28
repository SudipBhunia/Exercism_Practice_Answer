def line_up(name, number):
    if str(number)[-1] == '1':
        if str(number)[len(str(number))-2:] != '11':
            return f"{name}, you are the {number}st customer we serve today. Thank you!"
        else:
            return f"{name}, you are the {number}th customer we serve today. Thank you!"
    if str(number)[-1] == '2':
        if str(number)[len(str(number))-2:] == '12':
            return f"{name}, you are the {number}th customer we serve today. Thank you!"
        else:
            return f"{name}, you are the {number}nd customer we serve today. Thank you!"
    if str(number)[-1] == '3':
        if str(number)[len(str(number))-2:] == '13':
            return f"{name}, you are the {number}th customer we serve today. Thank you!"
        else:
            return f"{name}, you are the {number}rd customer we serve today. Thank you!"
    else:
        return f"{name}, you are the {number}th customer we serve today. Thank you!"
def line_up(name, number):
    suffixes = {'1':'st', '2':'nd', '3':'rd'}
    if str(number)[-1] in suffixes and str(number)[-2:] not in ['11', '12', '13']:
        suffix = suffixes[str(number)[-1]]
    else:
        suffix = 'th'
    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"
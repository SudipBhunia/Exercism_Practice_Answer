BRAC = '[{()}]'
PAIR = {
    ']' : '[',
    '}' : '{',
    ')' : '('
}
def is_paired(input_string):
    stac = []
    for i in range(len(input_string)):
        if input_string[i] in BRAC:
            stac.append(input_string[i])
            if input_string[i] in PAIR:
                if stac[len(stac) - 2] == PAIR[input_string[i]]:
                    stac.pop()
                    stac.pop()   
    return len(stac) == 0
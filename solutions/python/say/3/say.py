ones = lambda x: 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen nineteen'.split()[x]
tens = lambda x: 'zero ten twenty thirty forty fifty sixty seventy eighty ninety'.split()[x]
_say = lambda x: say(x)

cases = [  
    (  20,          1, ones, '',  ''),
    ( 1e2,         10, tens, '', '-'),
    ( 1e3,        100, ones, ' hundred', ' '),
    ( 1e6,       1000, _say, ' thousand', ' '),
    ( 1e9,    1000000, _say, ' million', ' '),
    (1e12, 1000000000, _say, ' billion', ' ')    
]

def say(number):
    v = lambda f, q, r, t, h: f(q) + t
    w = lambda f, q, r, t, h: f(q) + t + h + say(r)
 
    if (0 <= number < 1e12): 
        for condition, divider, func, txt, hyphen in cases:
            if number < condition:
                q, r = divmod(number, divider)                                     
                return {0: v}.get(r, w)(func, q, r, txt, hyphen)
                
    raise ValueError("input out of range")
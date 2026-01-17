def response(hey_bob):
    hey_bob = hey_bob.rstrip()
    if hey_bob.isupper() and hey_bob.endswith('?'):
        return "Calm down, I know what I'm doing!"
    if hey_bob.endswith('?'):
        return 'Sure.'
    if hey_bob.isupper():
        return "Whoa, chill out!"
    if len(hey_bob) == 0:
        return "Fine. Be that way!" 
    return 'Whatever.'
    
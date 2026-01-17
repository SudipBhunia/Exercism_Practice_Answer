def is_vowel(ch):
    vowel = 'aeiou'
    return ch in vowel

def func(text):
    i = 0
    while(not is_vowel(text[i])):
        i+=1
    text = text[i:] + text[:i]
    return text + 'ay'  
    
def translate(text):
    li = text.split(' ')
    for i in range(len(li)):
        text = li[i]
        if is_vowel(text[0]) or text.startswith('xr') or text.startswith('yt'):
            li[i] = text + 'ay'
        elif not is_vowel(text[0]):
            if 'qu' in text:
                flag = 0
                temp = text[:text.index('q')] 
                for j in temp:
                    if is_vowel(j):
                        flag = 1
                if flag == 1:
                    li[i] = func(text)
                else:
                    text = text[text.index('qu')+2:] + text[:text.index('q')+2]
                    li[i] = text + 'ay'
            elif 'y' in text[1:]:
                flag = 0
                temp = text[:text.index('y')] 
                for j in temp:
                    if is_vowel(j):
                        flag = 1
                if flag == 1:
                    li[i] = func(text)
                else:
                    text = text[text.index('y'):] + text[:text.index('y')]
                    li[i] = text + 'ay'
            else:
                li[i] = func(text)
    return ' '.join(li)
    

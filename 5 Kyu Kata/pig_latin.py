# Code by Tajrina Promela
# Date 14th November 2022, 12:15 PM
# Program that adds 'ay' to each word after moving its first letter to its end in Python

def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())
print(pig_it('Pig it !'))


import string
def pig_it(text):
    res = []
    punc = []
    lst = list(map(str, text.split()))
    for item in lst:
        if item in string.punctuation:
            punc.append(' ' + item)  
            break          
        else:
            word = item[1:] + item[0] + ''.join('ay')
        res.append(word)
    strn = ' '.join(res) + ''.join(punc)
    return strn
       
print(pig_it('Pig it !'))

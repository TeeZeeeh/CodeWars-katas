# Code by Tajrina Promela
# Date 6th November 2022, 2:00 PM
# Program to reverse words with 5 letters on more in a string in Python


def spin_words(sentence):
    a = sentence.split()
    for i in range(len(a)):
        if len(a[i]) >= 5:
            b = a[i]
            c = b[::-1]
            sentence = sentence.replace(a[i], c)
    return sentence
    
print(spin_words("Hey fellow warriors"))
print(spin_words("This is a test"))
print(spin_words("This is another test"))

def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext

with open('pap.txt') as book:
    haha = ''
    for line in book:
        for word in cleanedup(line).split():
            haha = max(len(word))
print(haha)

def cleanup(s):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    cleantext = ''
    for character in s.lower():
        if character in alph:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext

listt = {}
with open('pap.txt') as book:
    ln = 1
    for line in book:
        for word in cleanup(line).split():
            if word in listt:
                listt[word].append(ln)
            else:
                listt[word]=[ln]
        ln += 1

while True:
    word = input('Enter thing bro: ')
    if word in listt:
        print('Found here bruv: ', listt[word])
    else:
        print('nah son')

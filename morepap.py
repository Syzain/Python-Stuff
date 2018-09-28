repeat = {}
with open('pap.txt') as book:
    ln = 1
    for line in book:
        for word in line.split():
            if word in repeat:
                repeat[word].append(ln)
            else:
                repeat[word] = [ln]
        ln += 1

while True:
    word = input('Enter: ')
    if word in repeat:
        print ('Found here: ', repeat[word])
    else:
        print('not found bro')
            

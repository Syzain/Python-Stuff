count = 0
with open('pap.txt') as book:
    for line in book:
        for word in line:
            for letter in word.split():
                if letter == 'e':
                    count += 1
print("Number of times 'e' is used:", count)

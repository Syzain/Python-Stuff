count = 0
with open('pap.txt') as book:
    for line in book:
        for word in line.split():
            if(word == 'for' or 'for' in word):
                count+=1
print("Number of times 'for' is used:", count)

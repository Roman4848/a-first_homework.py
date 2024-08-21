string = ''
for k in range(3, 21):
    string = ''
    for i in range(1, k):
        for j in range(i + 1, k):
            if k % (i + j) == 0:
                string += str(i) + str(j)
    print(k, '-', string)


for k in range(3, 21):
    string = ''
    for i in range(1, k):
        for j in range(i + 1, k):
            if k % (i + j) == 0:
                string += str(i) + '+' + str(j) + ' '
    print(k, '-', string)
M = []
op = input()

for i in range(12):

    M.append([])
    for j in range(12):

        N = float(input())
        M[i].append(N)

s = 0
cont = 0
col = 1
for i in range(1, 11):

    for j in range(col):

        s += M[i][j]
        cont += 1

    if(i < 5):

        col += 1

    elif(i > 5):

        col -= 1

med = s / cont

if(op == "S"):

    print('{:.1f}'.format(s))

else:
    
    print('{:.1f}'.format(med))
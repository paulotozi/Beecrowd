M = []
op = input()

for i in range(12):

    M.append([])
    for j in range(12):

        N = float(input())
        M[i].append(N)

s = 0
inf = 1
sup = 11
cont = 0
for i in range(0,5):

    for j in range(inf,sup):

        s += M[i][j]
        cont += 1

    inf += 1
    sup -= 1

med = s / cont

if(op == "S"):

    print('{:.1f}'.format(s))

else:
    
    print('{:.1f}'.format(med))
    
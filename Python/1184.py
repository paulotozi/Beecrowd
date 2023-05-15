op = input()
M = [[0 for x in range(12)] for y in range(12)]

for i in range(12):

    for j in range(12):

        N = float(input())
        M[i][j] = N

if(op == 'S'):

    soma = 0.0

    for i in range(12):

        for j in range(12):

            if(i > j):

                soma += M[i][j]

    print("{:.1f}".format(soma))

if(op == 'M'):

    soma = 0
    c = 0

    for i in range(12):

        for j in range(12):

            if(i > j):

                soma += M[i][j]
                c += 1

    med = soma / c
    print("{:.1f}".format(med))
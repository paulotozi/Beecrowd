lin = int(input())
op = input()
M = [[0 for x in range(12)] for y in range(12)] 

for i in range(12):

    for j in range(12):

        N = float(input())
        M[i][j] = N
#print(M)
if(op == 'S'):

    soma = 0.0

    for i in range(12):

        soma += M[lin][i]

    print("{:.1f}".format(soma))

if(op == 'M'):

    soma = 0

    for i in range(12):

        soma += M[lin][i]

    med = soma / 12
    print("{:.1f}".format(med))
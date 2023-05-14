col = int(input())
op = input()
M = [[0 for x in range(12)] for y in range(12)] 

for i in range(12):

    for j in range(12):

        N = float(input())
        M[i][j] = N

if(op == 'S'):

    somas = 0.0

    for j in range(12):

        somas += M[j][col]

    print("{:.1f}".format(somas))

if(op == 'M'):

    somam = 0

    for j in range(12):

        somam += M[j][col]

    med = somam / 12
    print("{:.1f}".format(med))
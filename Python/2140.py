notas = [2, 5, 10, 20, 50, 100]

while(True):

    N, M = map(int, input().split())

    troco = M - N
    c = 0

    if(N == 0 and M == 0):

        break

    for i in notas:

        for j in notas:

            if(i + j == troco):

                c += 1
            
    if(c == 0):

        print("impossible")

    else:

        print("possible")
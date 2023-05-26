N = int(input())
tot = 0.0

for _ in range(N):

    cod, u = map(float, input().split())
    if(int(cod) == 1001):

        tot += (1.5 * u)

    elif(int(cod) == 1002):

        tot += (2.5 * u)

    elif(int(cod) == 1003):

        tot += (3.5 * u)

    elif(int(cod) == 1004):

        tot += (4.5 * u)

    elif(int(cod) == 1005):

        tot += (5.5 * u)

print("{:.2f}".format(tot))
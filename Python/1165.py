N = int(input())

for _ in range(N):

    num = int(input())
    prim = 0
    i = 1

    while(i <= num):

        if(num % i == 0):

            prim += 1

        i += 1

    if(prim > 2):

        print("{} nao eh primo".format(num))

    else:

        print("{} eh primo".format(num))
while(True):

    try:

        N = int(input())
        V = input().split()
        maior = 0

        for i in range(N):

            if(int(V[i]) >= maior):

                maior = int(V[i])

        if(maior < 10):

            print(1)

        elif(maior >= 10 and maior < 20):

            print(2)

        elif(maior >= 20):

            print(3)

    except EOFError:

        break        
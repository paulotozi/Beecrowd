while(True):

    try:

        N = int(input())

        M = []

        for i in range(0, N):

            M.append([])
            for j in range(0, N):

                M[i].append('3')

            c1 = N - 1
          
        for i in range(0,N):

            M[i][i] = '1'
            M[i][c1] = '2'
            c1 -= 1
            m = ''.join(M[i])
            print(m)

    except EOFError:

        break
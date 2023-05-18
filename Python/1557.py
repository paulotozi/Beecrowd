N = 9999

while(True):

    N = int(input())

    if(N == 0):

        break
    
    M = list()

    for i in range(N):

        M.append([])
        for j in range(N):

            M[i].append(0)

    M[0][0] = 1
    for i in range(0,N):

        if(i >= 1):

            M[i][0] = M[i - 1][0] * 2
            
        for j in range(1, N):

            M[i][j] = M[i][j-1] * 2

    T = len(str(M[N - 1][N - 1]))
    for i in range(N):

        for j in range(N):

            M[i][j] = str(M[i][j])
            while(len(M[i][j]) < T):

                M[i][j] = ' ' + M[i][j]

        m = ' '.join(M[i])
        
        print(m)

    print()
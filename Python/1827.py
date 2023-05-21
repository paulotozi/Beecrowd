while True:
    
    try:
        N = int(input())
        s = int(N / 3)
        e = N - s
        
        M = [[0 for i in range(N)] for j in range(N)]
        
        for i in range(N):
            
            M[i][i] = 2
            
        j = 0
        for i in range(N - 1, -1, -1):
            
            M[j][i] = 3
            j += 1
        
        for i in range(s, e):

            for j in range(s, e):
                
                M[i][j] = 1
        
        M[int(N / 2)][int(N / 2)] = 4
        
        for i in range(N):

            for j in range(N):

                print(M[j][i], end='')

            print()

        print()
    
    except EOFError:
        
        break
s = 0

while(s == 0):

    N = int(input())

    if(N == 0):

        s = 1

    else:
        st = ""
        for i in range(1, N + 1):

            if(i == N):

                st += str(N)
            
            else:

                st += "{} ".format(i)
        
        print(st)
N = int(input())

for _ in range(N):

    n1, n2 = input().split()
    soma = 0
    i = int(n1)
    c = 0

    while(c != int(n2)):

        if(i % 2 != 0):

            c += 1
            soma += i
        
        i += 1

    print(soma)

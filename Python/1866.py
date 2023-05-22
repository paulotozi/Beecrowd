N = int(input())

for _ in range(N):
    
    num = int(input())
    soma = 1

    for i in range(num - 1):

        if(i % 2 == 0):

            soma -= 1

        elif(i % 2 != 0):

            soma += 1

    print(soma)
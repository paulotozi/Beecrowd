N = int(input())

for _ in range(N):

    x, y = input().split()

    if(int(y) == 0):

        print("divisao impossivel")

    else:

        print(int(x) / int(y))
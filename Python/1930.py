N = list(map(int, input().split()))
soma = 0

for i in range(4):

    if(i == 3):

        soma += N[i]

    else:

        soma += (N[i] - 1)

print(soma)
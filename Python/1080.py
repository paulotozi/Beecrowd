arr = []
maior = 0
idx = 0 

for _ in range(100):

    N = int(input())

    arr.append(N)

    if(N > maior):

        maior = N
        idx = arr.index(N)

print(maior)
print(idx + 1)




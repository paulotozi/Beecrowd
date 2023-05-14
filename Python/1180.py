N = int(input())
arr = input().split()
menor = 1000
idx = 0

for i in range(len(arr)):

    num = int(arr[i])
    if(num < menor):

        menor = num
        idx = i

print("Menor valor: {}".format(menor))
print("Posicao: {}".format(idx))



    


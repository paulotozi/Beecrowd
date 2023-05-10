n1 = int(input())
n2 = int(input())
soma = 0

if(n1 > n2):

    a = n2
    b = n1

elif(n1 <= n2):

    a = n1
    b = n2


while(a <= b):

    if(a % 13 != 0):

        soma += a
    
    a += 1

print(soma)
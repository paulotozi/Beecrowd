par = 0
impar = 0
pos = 0
neg = 0

for _ in range(5):

    N = int(input())

    if(N % 2 == 0):

        par += 1

    elif(N % 2 != 0):

        impar += 1

    if(N > 0):

        pos += 1

    elif(N < 0):

        neg += 1

print("{} valor(es) par(es)".format(par))
print("{} valor(es) impar(es)".format(impar))
print("{} valor(es) positivo(s)".format(pos))
print("{} valor(es) negativo(s)".format(neg))


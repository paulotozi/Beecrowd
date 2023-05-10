s = 1
c = 0
soma = 0

while(s == 1):

    if(c == 2):

        break

    N = float(input())
    if(N >= 0.0 and N <= 10.0):

        c += 1
        soma += N

    else:

        print("nota invalida")

print("media = {:.2f}".format(soma / c))
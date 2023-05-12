s = 0
a = 0
g = 0
d = 0
print("MUITO OBRIGADO")

while(s == 0):

    N = int(input())

    if(N == 4):

        s = 1

    elif(N == 1):

        a += 1

    elif(N == 2):

        g += 1

    elif(N == 3):

        d += 1

print("Alcool: {}".format(a))
print("Gasolina: {}".format(g))
print("Diesel: {}".format(d))
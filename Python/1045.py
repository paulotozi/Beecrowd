N = input().split()
for i in range(len(N)):

    N[i] = float(N[i])

N.sort(reverse = True)

a = N[0]
b = N[1]
c = N[2]

if(a >= b + c):

    print("NAO FORMA TRIANGULO")

elif((a ** 2) == (b ** 2) + (c ** 2)):

    print("TRIANGULO RETANGULO")

elif((a ** 2) > (b ** 2) + (c ** 2)):

    print("TRIANGULO OBTUSANGULO")

elif((a ** 2) < (b ** 2) + (c ** 2)):

    print("TRIANGULO ACUTANGULO")

if(a == b and b == c):

    print("TRIANGULO EQUILATERO")

elif(a == b or b == c):

    print("TRIANGULO ISOSCELES")

N = input().split(" ")

A, B, C = N

MaiorAB = (int(A) + int(B) + abs(int(A) - int(B))) // 2

Maior = (MaiorAB + int(C) + abs(MaiorAB - int(C))) // 2

print("{} eh o maior".format(Maior))

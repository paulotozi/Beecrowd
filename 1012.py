N = input().split(" ")

A, B, C = N

TRIANGULO = float(A) * float(C) / 2

CIRCULO = 3.14159 * (float(C) ** 2) 

TRAPEZIO = (float(A) + float(B)) * float(C) / 2

QUADRADO = float(B) ** 2

RETANGULO = float(A) * float(B)

print("TRIANGULO: {}".format("{:.3f}".format(TRIANGULO)))
print("CIRCULO: {}".format("{:.3f}".format(CIRCULO)))
print("TRAPEZIO: {}".format("{:.3f}".format(TRAPEZIO)))
print("QUADRADO: {}".format("{:.3f}".format(QUADRADO)))
print("RETANGULO: {}".format("{:.3f}".format(RETANGULO)))

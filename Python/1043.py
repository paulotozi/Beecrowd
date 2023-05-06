N = input().split(" ")
a, b, c = N
a = float(a)
b = float(b)
c = float(c)

if(abs(a - c) < b < abs(a + c) and abs(b - c) < a < abs(b + c) and abs(a - b) < c < abs(a + b)):

    print("Perimetro = {}".format("{:.1f}".format(a + b + c)))

else:

    print("Area = {}".format("{:.1f}".format(((a + b) / 2) * c)))

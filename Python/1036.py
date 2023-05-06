N = input().split(" ")

a, b, c = N

a = float(a)
b = float(b)
c = float(c)

if(a != 0):

    delta = (b ** 2) - (4 * a * c)

    if(delta > 0):

        r1 = ((-b) + (delta ** (1 / 2))) / (2 * a)
        r2 = ((-b) - (delta ** (1 / 2))) / (2 * a)

        print("R1 = {}".format("{:.5f}".format(r1)))
        print("R2 = {}".format("{:.5f}".format(r2 )))

    else:

        print("Impossivel calcular")

else:

    print("Impossivel calcular")


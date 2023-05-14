n = 1
d = 0
i = 1
S = 0

while(n < 40):

    if(d == 0):

        S += n / 1
        n += 2
        d += 2 ** 1
        i += 1

    else:

        S += (n / d)
        n += 2
        d = 2 ** i
        i += 1

print("{:.2f}".format(S))
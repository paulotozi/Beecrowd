c = 0
med = 0.0

for _ in range(6):

    N = float(input())

    if(N > 0):

        c += 1
        med += N

print("{} valores positivos".format(c))
print("{:.1f}".format(med / c))
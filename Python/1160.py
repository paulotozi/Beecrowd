N = int(input())

for _ in range(0, N):

    pa, pb, g1, g2 = map(float, input().split())
    pa = int(pa)
    pb = int(pb)
    c = 0

    while(pb >= pa):

        pa = int(pa * (1 + (g1/100)))
        pb = int(pb * (1 + (g2/100)))
        c += 1

        if(c > 100):

            break

    if(c > 100):

        print("Mais de 1 seculo.")

    else:

        print("{} anos.".format(c))

    
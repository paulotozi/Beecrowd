N = int(input())

for _ in range(N):

    num = int(input())
    perf = 0
    c = 1

    while(perf < num):

        if(num == 1):

            break

        else:

            perf += c
            c += 1

    if(perf == num):

        print("{} eh perfeito".format(num))

    else:

        print("{} nao eh perfeito".format(num))
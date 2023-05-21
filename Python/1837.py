N = list(map(int, input().split()))

for r in range(abs(N[1])):

    if((N[0] - r) % N[1] == 0):

        a = N[0]
        b = N[1]
        print("{} {}".format(((a - r) // b), r))
        break
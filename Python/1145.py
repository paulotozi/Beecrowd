N = input().split()
c = 1

for i in range(1, int(int(N[1]) / int(N[0])) + 1):

    m = ""

    for _ in range(int(N[0])):

        m += str(c) + " "
        c += 1

    print(m[:-1])
s = 0
avg = 0
c = 0

while(s == 0):

    N = int(input())

    if(N < 0):

        s = 1

    else:

        avg += N
        c += 1

print("{:.2f}".format(avg / c))
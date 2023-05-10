N = int(input())

for _ in range(N):

    f = input().split()
    f1, f2, f3 = f

    print("{:.1f}".format(((float(f1) * 2) + (float(f2) * 3) + (float(f3) * 5)) / 10))
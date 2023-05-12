N = int(input())
num = 1

for _ in range(N):

    print("{} {} {}".format(num, num ** 2, num ** 3))
    print("{} {} {}".format(num, (num ** 2) + 1, (num ** 3) + 1))
    num += 1
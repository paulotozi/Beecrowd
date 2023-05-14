N = int(input())
arr = []
c = 0

for i in range(10):

    arr.append((N) * (2 ** c))
    c += 1
    print("N[{}] = {}".format(i, arr[i]))

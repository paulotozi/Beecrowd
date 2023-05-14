N = float(input())
arr =[]
c = 1
s = 0
count = 0

while(count < 100):

    c = 2 ** s
    arr.append(N / c)
    s += 1
    count += 1

for i in range(len(arr)):

    print("N[{}] = {:.4f}".format(i, arr[i]))
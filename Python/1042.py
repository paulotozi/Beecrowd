N = input().split(" ")
a, b, c = N
arr = []

for i in range(len(N)):

    arr += [int(N[i])]

arr_asc = sorted(arr)
for i in range(len(arr_asc)):

    print(arr_asc[i])

print("")

for i in range(len(arr)):

    print(arr[i])

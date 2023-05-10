N = int(input())

for _ in range(N):

    sum = 0
    num = input().split()
    n1, n2 = num
    arr = [int(n1)] + [int(n2)]
    arr.sort()
    for i in range(arr[0] + 1, arr[1]):

        if(i % 2 != 0):

            sum += i
    
    print(sum)
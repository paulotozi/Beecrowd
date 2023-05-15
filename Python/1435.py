while True:

    N = int(input())

    if (N == 0):

        break

    result =  []

    for i in range(N):

        tmp = []
        for j in range(N):

            tmp.append(1)

        result.append(tmp)

    value = 1
    up = 0
    left = 0
    down = N - 1
    right = N - 1

    if (N % 2 == 0):

        middle = N / 2

    else:

        middle = (N + 1) / 2


    while (value <= middle):

        i = left
        while (i <= right):

            result[up][i] = value
            result[down][i] = value
            i += 1

        i = (up + 1)
        while (i < down):

            result[i][left] = value
            result[i][right] = value
            i += 1

        value += 1
        up += 1
        down -= 1
        left += 1
        right -= 1

    for i in range(N):
        
        tx = ''
        for j in range(N):

            tx += " %3d" %result[i][j]

        print(tx[1:])

    print("")

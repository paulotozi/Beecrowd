arr =[]

for _ in range(10):

    N = int(input())

    if(N == 0 or N < 0):

        arr.append(1)
    
    else:

        arr.append(N)

for i in range(10):

    print("X[{}] = {}".format(i, arr[i]))
A= []

for i in range(100):

    N = float(input())
    A.append(N)
    if(N <= 10):

        print("A[{}] = {:.1f}".format(i, A[i]))

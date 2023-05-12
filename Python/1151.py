N = int(input())
fib = [0, 1]

if(N == 0):

    print(0)

else:

    for i in range(1, N - len(fib) + 1):

        fib += [fib[i - 1] + fib[i]]

s = ""
for i in range(len(fib)):

    if(i == len(fib) - 1):

        s += "{}".format(fib[i])

    else:

        s += "{} ".format(fib[i])

print(s)


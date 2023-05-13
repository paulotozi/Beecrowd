s = 0

while(s == 0):

    N = int(input())

    if(N == 0):

        s += 1

    else:

        i = N
        c = 0
        soma = 0

        while(c != 5):

            if(i % 2 == 0):

                soma += i
                c += 1

            i += 1

        print(soma)

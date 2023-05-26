caso = 1
while(True):

    try:

        N = int(input())
        order = ['0']

        for i in range(N + 1):

            for j in range(i):

                order.append(i)

        print("Caso {}: {} numero".format(caso, len(order)), end ='')

        if(N != 0):

            print('s', end='')

        print()

        for i in range(len(order)):

            print(order[i], end = '')

            if(i != len(order) - 1):

                print(' ', end = '')

            else:

                print()

        print()
        caso += 1
        
    except EOFError:
        
        break
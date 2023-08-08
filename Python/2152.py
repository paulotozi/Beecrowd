N = int(input())

porta = {1:"A porta abriu!", 0:"A porta fechou!"}

for _ in range(N):

    h, m, o = map(int, input().split())
    if(h < 10):

        if(m < 10):

            print("0{}:0{} - {}".format(h, m, porta[o]))

        else:

            print("0{}:{} - {}".format(h, m, porta[o]))

    else:

        if(m < 10):

            print("{}:0{} - {}".format(h, m, porta[o]))

        else:

            print("{}:{} - {}".format(h, m, porta[o]))
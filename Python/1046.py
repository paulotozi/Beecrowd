N = input().split()
hr1, hr2 = N
hr1 = int(hr1)
hr2 = int(hr2)

if(hr1 < hr2):

    print("O JOGO DUROU {} HORA(S)".format(hr2 - hr1))

else:

    print("O JOGO DUROU {} HORA(S)".format(hr2 + 24 - hr1))

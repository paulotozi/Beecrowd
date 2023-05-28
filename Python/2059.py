p, j1, j2, r, a = map(int, input().split())

soma = (j1 + j2) % 2

if(r == 1):

    if(a == 1):

        print("Jogador 2 ganha!")

    else:

        print("Jogador 1 ganha!")

else:

    if(p == 1):

        if(soma == 1):

            print("Jogador 2 ganha!")

        else:

            print("Jogador 1 ganha!")

    elif(p == 0):

        if(soma == 1):

            print("Jogador 1 ganha!")

        else:

            print("Jogador 2 ganha!")

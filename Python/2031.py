N = int(input())

for _ in range(N):

    p1 = input()
    p2 = input()

    if(p1 == "ataque"):

        if(p2 == "pedra"):

            print("Jogador 1 venceu")

        elif(p2 == "papel"):

            print("Jogador 1 venceu")

        elif(p2 == "ataque"):

            print("Aniquilacao mutua")

    elif(p1 == "pedra"):

        if(p2 == "papel"):

            print("Jogador 1 venceu")

        elif(p2 == "ataque"):

            print("Jogador 2 venceu")

        elif(p2 == "pedra"):

            print("Sem ganhador")

    elif(p1 == "papel"):

        if(p2 == "ataque"):

            print("Jogador 2 venceu")

        elif(p2 == "pedra"):

            print("Jogador 2 venceu")

        elif(p2 == "papel"):

            print("Ambos venceram")
N = int(input())
c = 1

for _ in range(N):

    s = input().split()

    if(s[0] == "tesoura"):

        if(s[1] == "papel"):

            print("Caso #{}: Bazinga!".format(c))
            c += 1

        elif(s[1] == "Spock"):

            print("Caso #{}: Raj trapaceou!".format(c))
            c += 1

        elif(s[1] == "lagarto"):

            print("Caso #{}: Bazinga!".format(c))
            c += 1

        elif(s[1] == "pedra"):

            print("Caso #{}: Raj trapaceou!".format(c))
            c += 1

        elif(s[1] == "tesoura"):

            print("Caso #{}: De novo!".format(c))
            c += 1

    elif(s[0] == "papel"):

        if(s[1] == "pedra"):

            print("Caso #{}: Bazinga!".format(c))
            c += 1

        elif(s[1] == "Spock"):

            print("Caso #{}: Bazinga!".format(c))
            c += 1

        elif(s[1] == "lagarto"):

            print("Caso #{}: Raj trapaceou!".format(c))
            c += 1

        elif(s[1] == "tesoura"):

            print("Caso #{}: Raj trapaceou!".format(c))
            c += 1

        elif(s[1] == "papel"):

            print("Caso #{}: De novo!".format(c))
            c += 1

    elif(s[0] == "pedra"):

        if(s[1] == "pedra"):

            print("Caso #{}: De novo!".format(c))
            c += 1

        elif(s[1] == "Spock"):

            print("Caso #{}: Raj trapaceou!".format(c))
            c += 1

        elif(s[1] == "lagarto"):

            print("Caso #{}: Bazinga!".format(c))
            c += 1

        elif(s[1] == "tesoura"):

            print("Caso #{}: Bazinga!".format(c))
            c += 1

        elif(s[1] == "papel"):

            print("Caso #{}: Raj trapaceou!".format(c))
            c += 1

    elif(s[0] == "lagarto"):

        if(s[1] == "pedra"):

            print("Caso #{}: Raj trapaceou!".format(c))
            c += 1

        elif(s[1] == "Spock"):

            print("Caso #{}: Bazinga!".format(c))
            c += 1

        elif(s[1] == "lagarto"):

            print("Caso #{}: De novo!".format(c))
            c += 1

        elif(s[1] == "tesoura"):

            print("Caso #{}: Raj trapaceou!".format(c))
            c += 1

        elif(s[1] == "papel"):

            print("Caso #{}: Bazinga!".format(c))
            c += 1

    elif(s[0] == "Spock"):

        if(s[1] == "pedra"):

            print("Caso #{}: Bazinga!".format(c))
            c += 1

        elif(s[1] == "Spock"):

            print("Caso #{}: De novo!".format(c))
            c += 1

        elif(s[1] == "lagarto"):

            print("Caso #{}: Raj trapaceou!".format(c))
            c += 1

        elif(s[1] == "tesoura"):

            print("Caso #{}: Bazinga!".format(c))
            c += 1

        elif(s[1] == "papel"):

            print("Caso #{}: Raj trapaceou!".format(c))
            c += 1
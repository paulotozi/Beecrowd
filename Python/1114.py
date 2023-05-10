s = 1

while(s == 1):

    N = input()
    senha = "2002"
    c = 1

    for i in range(len(senha)):

        if(N[i] != senha[i]):

            print("Senha Invalida")
            break

        else:

            c += 1

    if(N == "2002"):

        print("Acesso Permitido")
        s = 0

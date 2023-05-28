caso = 1
while(True):
    
    try:

        n1 = input()
        n2 = input()

        print('Caso #{}:'.format(caso))
        
        qtd = n2.count(n1)
        if(qtd == 0):

            print("Nao existe subsequencia")

        else:

            print("Qtd.Subsequencias: {}".format(qtd))
            qtd = n2.rfind(n1)
            print("Pos: {}".format((int(qtd)+1)))

        print()

        caso += 1
        
    except EOFError:

        break
s = 1
c = 0  
soma = 0

while(s == 1):
    
    N = float(input())
    if(N >= 0.0 and N <= 10.0):

        c += 1
        soma += N
        if(c == 2):

            print("media = {:.2f}".format(soma / c))
            c = 0
            soma = 0

            while(True):

                print("novo calculo (1-sim 2-nao)")
                msg = int(input())
                if(msg == 2):

                    s = 0
                    break

                elif(msg == 1):

                    break

    else:

        print("nota invalida")

    
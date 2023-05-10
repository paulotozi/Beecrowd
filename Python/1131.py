s = True
grenais = 0
inter = 0
gremio = 0
empates = 0
N = 1

while(s == True):
    
    if(N == 2):

        s = False

    else:

        a, b = input().split()
        if(int(a) > int(b)):

            grenais += 1
            inter += 1

        elif(int(a) < int(b)):

            grenais += 1
            gremio += 1

        elif(int(a) == int(b)):

            grenais += 1
            empates += 1

    print("Novo grenal (1-sim 2-nao)")
    N = int(input())
    if(N == 2):

        break
    

print("{} grenais".format(grenais))
print("Inter:{}".format(inter))
print("Gremio:{}".format(gremio))
print("Empates:{}".format(empates))

if(inter > gremio):

    print("Inter venceu mais")

elif(inter < gremio):

    print("Gremio venceu mais")

else:

    print("Nao houve vencedores")
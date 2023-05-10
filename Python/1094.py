cobaia = 0
coelho = 0
rato = 0
sapo = 0
por_c = 0.0
por_r = 0.0
por_s = 0.0

N = int(input())
for _ in range(N):

    st = input().split()
    amt, tipo = st

    if(tipo == 'C'):

        coelho += int(amt)
        cobaia += int(amt)

    elif(tipo == 'R'):

        rato += int(amt)
        cobaia += int(amt)

    elif(tipo == 'S'):

        sapo += int(amt)
        cobaia += int(amt)

por_c = (coelho / cobaia) * 100
por_r = (rato / cobaia) * 100
por_s = (sapo / cobaia) * 100

print("Total: {} cobaias".format(cobaia))
print("Total de coelhos: {}".format(coelho))
print("Total de ratos: {}".format(rato))
print("Total de sapos: {}".format(sapo))
print("Percentual de coelhos: {:.2f} %".format(por_c))
print("Percentual de ratos: {:.2f} %".format(por_r))
print("Percentual de sapos: {:.2f} %".format(por_s))

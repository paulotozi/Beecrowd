BRL = float(input())

CEM = BRL // 100
BRL -= CEM * 100

CINQUENTA = BRL // 50
BRL -= CINQUENTA * 50

VINTE = BRL // 20
BRL -= VINTE * 20

DEZ = BRL // 10
BRL -= DEZ * 10 

CINCO = BRL // 5
BRL -= CINCO * 5

DOIS = BRL // 2
BRL -= DOIS * 2

UM = BRL // 1
BRL -= UM

cinq_cent = BRL // 0.50
BRL -= cinq_cent * 0.50

vincin_cent = BRL // 0.25
BRL -= vincin_cent * 0.25

dez_cent = BRL // 0.10
BRL -= dez_cent * 0.10

cinc_cent = BRL // 0.05
BRL -= cinc_cent * 0.05

um_cent = BRL / 0.01
BRL -= um_cent * 0.01

print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(int(CEM)))
print("{} nota(s) de R$ 50.00".format(int(CINQUENTA)))
print("{} nota(s) de R$ 20.00".format(int(VINTE)))
print("{} nota(s) de R$ 10.00".format(int(DEZ)))
print("{} nota(s) de R$ 5.00".format(int(CINCO)))
print("{} nota(s) de R$ 2.00".format(int(DOIS)))
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(int(UM)))
print("{} moeda(s) de R$ 0.50".format(int(cinq_cent)))
print("{} moeda(s) de R$ 0.25".format(int(vincin_cent)))
print("{} moeda(s) de R$ 0.10".format(int(dez_cent)))
print("{} moeda(s) de R$ 0.05".format(int(cinc_cent)))
print("{} moeda(s) de R$ 0.01".format(round(um_cent)))
BRL = int(input())
print(BRL)

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

print("{} nota(s) de R$ 100,00".format(CEM))
#print(BRL)
print("{} nota(s) de R$ 50,00".format(CINQUENTA))
print("{} nota(s) de R$ 20,00".format(VINTE))
print("{} nota(s) de R$ 10,00".format(DEZ))
print("{} nota(s) de R$ 5,00".format(CINCO))
print("{} nota(s) de R$ 2,00".format(DOIS))
print("{} nota(s) de R$ 1,00".format(UM))

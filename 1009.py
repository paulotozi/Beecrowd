# -*- coding: utf-8 -*-

NOME = input()
SALARIO = float(input())
VENDA = float(input())

TOTAL = SALARIO + (VENDA * 0.15)

print("TOTAL = R$ {}".format("{:.2f}".format(TOTAL)))


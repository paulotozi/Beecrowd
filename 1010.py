# -*- coding: utf-8 -*-

A = input().split(" ")
B = input().split(" ")

COD1, QTD1, PRECO1 = A
COD2, QTD2, PRECO2 = B

TOTAL = (float(PRECO1) * int(QTD1)) + (float(PRECO2) * int(QTD2))

print("VALOR A PAGAR: R$ {}".format("{:.2f}".format(TOTAL)))

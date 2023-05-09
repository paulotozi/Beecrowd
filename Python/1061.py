dia, dia1 = input().split()
dia1 = int(dia1)
hora1, min1, seg1 = map(int,input().split(":"))
min1 = int(min1)

dia, dia2 = input().split()
dia2 = int(dia2)
hora2, min2, seg2 = map(int,input().split(":"))
min2 = int(min2)

seg = seg2 - seg1
mts = min2 - min1
hora = hora2 - hora1
dia = dia2 - dia1

if(seg < 0):
	seg += 60
	mts = mts - 1


if(mts < 0):
	mts += 60
	hora -= 1

if(hora < 0):
	hora += 24
	dia -= 1

print("{} dia(s)".format(dia))
print("{} hora(s)".format(hora))
print("{} minuto(s)".format(mts))
print("{} segundo(s)".format(seg))
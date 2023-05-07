hr1, min1, hr2, min2 = list(map(int,input().split()))

dif = ((hr2 * 60) + min2) - ((hr1 * 60) + min1)
if(dif <= 0):

    dif += 24 * 60
    
hr = dif // 60
minuto = dif % 60
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hr, minuto))
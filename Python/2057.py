h1, h2, f_hr = map(int, input().split())

hora = h1 + h2

hora_final = hora + f_hr

if(hora_final > 24):

    hora_final -= 24
    print(hora_final)

elif(hora_final < 0):

    hora_final += 24
    print(hora_final)

else:

    print(hora_final)
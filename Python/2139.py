mss = {"1":31, "2":29, "3":31, "4":30, "5":31, "6":30, "7":31, "8":31, "9":30, "10":31, "11":30, "12":31}

def natal(mes, dia):

    if(mes == 12):

        if(dia == 25):

            return "E natal!"

        elif(dia > 25):

            return "Ja passou!"
        
        elif(dia == 24):

            return "E vespera de natal!"

        else:

            return "Faltam {} dias para o natal!".format(25 - dia)

    else:

        sum_dia = 0
        sum_dia += int(mss[str(mes)])

        for i in range(mes + 1, 12):

            sum_dia += int(mss[str(i)])


        sum_dia += (25 - dia)

        return "Faltam {} dias para o natal!".format(sum_dia)

while(True):

    try:

        mes, dia = map(int,input().split())

        print(natal(mes, dia))

    except EOFError:

        break   

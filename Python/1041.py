coord = input().split(" ")
x, y = coord
x = float(x)
y = float(y)

if(x > 0):

    if(y > 0):

        print("Q1")

    elif(y < 0):

        print("Q4")

elif(x < 0):

    if(y > 0):

        print("Q2")

    elif(y < 0):

        print("Q3")

elif(x == 0):

    if(y == 0):

        print("Origem")

    else:

        print("Eixo Y")

if(y == 0):

    if(x != 0):

        print("Eixo X")
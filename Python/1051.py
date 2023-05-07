s = float(input())

if(s <= 2000):

    i = 0
    print("Isento")

if(s > 2000 and s <= 3000):

    s_8 = s - 2000
    i = s_8 * 0.08

if(s > 3000 and s <= 4500):

    i_8 = 0.08 * 1000
    s_18 = s - 3000
    i = s_18 * 0.18 + i_8

if(s > 4500):

    i_8 = 0.08 * 1000
    i_18 = 0.18 * 1500
    s_28 = s - 4500
    i = i_18 + i_8 + s_28 * 0.28

if(s > 2000):

    i = float(i)
    print("R$ {:.2f}".format(i))
    
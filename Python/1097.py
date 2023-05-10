I = 1
J = 7

while(I != 10):

    if(I % 2 != 0):

        for i in range(3):

            print("I={} J={}".format(I, J - i))
        
        J += 2

    I += 1

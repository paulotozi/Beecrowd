I = 0
J = 1

while(I <= 2):
             
    if(I % 1 == 0 and J % 1 == 0):

        I = int(I)
        J = int(J)

        for i in range(3):

            print("I={} J={}".format(round(I), round(J + i)))
    
    elif(I == 1.9999999999999998):

        for i in range(3):

            print("I={} J={}".format(round(I), round(J + i)))
    
    elif(I == 1.0):

        for i in range(3):

            print("I={} J={}".format(int(I), round(J + i)))

    else:

        for i in range(3):
    
            print("I={:.1f} J={:.1f}".format(I, J + i))
        
    J += 0.2
    I += 0.2

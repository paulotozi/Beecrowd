N = int(input())

while(N > 0):

    if(N >= 1000):

        print('M',end='')
        N-= 1000

    elif(N>=900):

        print('CM',end='')
        N-= 900

    elif(N >= 500):

        print('D',end='')
        N-= 500

    elif(N >= 400):

        print('CD',end='')
        N-= 400

    elif(N >= 100):

        print('C',end='')
        N-= 100

    elif(N >= 90):

        print('XC',end='')
        N-= 90

    elif(N >= 50):

        print('L',end='')
        N -= 50

    elif(N >= 40):

        print('XL',end='')
        N-= 40

    elif(N >= 10):

        print('X',end='')
        N -= 10

    elif(N >= 9):

        print('IX',end='')
        N-= 9
        
    elif(N >= 5):

        print('V',end='')
        N-= 5

    elif(N >= 4):

        print('IV',end='')
        N-= 4

    elif(N >= 1):

        print('I',end='')
        N-= 1
        
print()
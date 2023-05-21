def blink_bin(blink):

    blink = blink.replace('-','0')
    blink = blink.replace('*','1')
    return blink


def bin_int(blink):

    blink = int(blink, 2)
    return blink


def soma(blink, s):

    s += blink
    return s

def main():

    for i in range(3):
        
        s = 0
        while True:

            blink = input()
            if(blink != 'caw caw'):

                blink = blink_bin(blink)
                blink = bin_int(blink)
                s = soma(blink, s)

            else:
                
                print(s)
                break

main()
    
def dec_hexa(dec):
    
    hexa = hex(dec)
    hexa = hexa[2:]
    return hexa

def main(hexa):
    
    hexa = hexa.upper()
    print(hexa)

main(dec_hexa(int(input())))

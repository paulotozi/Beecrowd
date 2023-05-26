while(True):

    try:

        hr = input().split(':')

        atraso = int(hr[0]) * 60 + int(hr[1]) - 420
        if(atraso < 0):

            atraso = 0

        print('Atraso maximo: %d' % atraso)
        
    except EOFError:
        
        break
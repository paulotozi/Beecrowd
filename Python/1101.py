s = 1

while(s == 1):

    N = input().split()
    arr = [int(N[0])] + [int(N[1])]
    arr.sort()

    if(arr[0] == 0 or arr[1] == 0):

        s = 0
    
    elif(arr[0] < 0 or arr[1] < 0):

        s = 0

    else:

        count = 0
        s_print = ""
        for i in range(arr[0], arr[1] + 1):

            s_print += "{} ".format(i)
            count += i

        print("{}Sum={}".format(s_print, count))

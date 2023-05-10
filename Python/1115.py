s = 1

while(s == 1):

    N = input().split()
    arr = [int(N[0])] + [int(N[1])]

    if(arr[0] == 0 or arr[1] == 0):

        s = 0

    elif(arr[0] > 0 and arr[1] > 0):

        print("primeiro")

    elif(arr[0] < 0 and arr[1] > 0):

        print("segundo")

    elif(arr[0] < 0 and arr[1] < 0):

        print("terceiro")

    elif(arr[0] > 0 and arr[1] < 0):

        print("quarto")
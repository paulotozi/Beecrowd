s = 1

while(s == 1):

    N = input().split()
    arr = [int(N[0])] + [int(N[1])]

    if(N[0] == N[1]):

        s = 0

    elif(arr == sorted(arr, reverse = True)):

        print("Decrescente")

    elif(arr == sorted(arr)):

        print("Crescente")
N = list(map(int, input().split()))

if(N[0] > N[1]):

    if(N[2] > N[1]):

        print(":)")

    else:
        
        if((N[1] - N[2]) < (N[0] - N[1])):

            print(":)")

        else:

            print(":(")
            
elif(N[0] < N[1]):

    if(N[2] < N[1]):

        print(":(")

    else:

        if((N[1] - N[2]) > (N[0] - N[1])):

            print(":(")

        else:

            print(":)")

else:

    if(N[2] > N[1]):

        print(":)")

    else:

        print(":(")
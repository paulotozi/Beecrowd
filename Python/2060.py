N = int(input())

arr = list(map(int, input().split()))

dois = 0
tres = 0
quatro = 0
cinco = 0

for i in range(N):

    if(arr[i] % 2 == 0):

        dois += 1

    if(arr[i] % 3 == 0):

        tres += 1

    if(arr[i] % 4 == 0):

        quatro += 1

    if(arr[i] % 5 == 0):

        cinco += 1


print("{} Multiplo(s) de 2".format(dois))
print("{} Multiplo(s) de 3".format(tres))
print("{} Multiplo(s) de 4".format(quatro))
print("{} Multiplo(s) de 5".format(cinco))
arr = []
for _ in range(6):
    
    arr.append(float(input()))

c = 0
for i in range(len(arr)):

    if(arr[i] > 0):

        c += 1

print("{} valores positivos".format(c))
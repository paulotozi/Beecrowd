dentro = 0
fora = 0
N = int(input())
arr = []

for _ in range(N):

    num = input()
    #print(num)
    arr.append(int(num))

for i in range(len(arr)):

    if(arr[i] >= 10 and arr[i] <= 20):

        dentro += 1
    
    else:

        fora += 1

print("{} in".format(dentro))
print("{} out".format(fora))
N = list(map(int, input().split()))
i = 1
s = 0

while(N[i] <= 0):

    if(N[i] <= 0):

        i += 1

    if(N[i] > 0):

        break

for c in range(N[i]):

    s += N[0] + c

print(s)
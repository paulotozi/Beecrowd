N = int(input())
con = list(map(int, input().split()))
c = 0

for i in range(len(con)):

    if(con[i] == N):

        c += 1

print(c)
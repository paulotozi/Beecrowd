N = int(input())
id = -1
temp_g = 0

for _ in range(N):

    iden, grd = map(float, input().split())
    if(grd > temp_g and grd >= 8):

        id = int(iden)
        temp_g = grd

if(id == -1):

    print("Minimum note not reached")

else:

    print(id)
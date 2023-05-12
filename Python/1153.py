N = int(input())
exp = 1
fat = N

while(exp != N):
    
    fat = fat * (N - exp)
    exp += 1

print(fat)
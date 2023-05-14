arr = []

for i in range(20):
    
    N = int(input())
    arr.append(N)

arr_temp = arr[::-1]
for i in range(20):
    
    print('N[{}] = {}'.format(i, arr_temp[i]))
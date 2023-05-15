M = []
op = input()

for i in range(12):

    M.append([])
    for j in range(12):

        N = float(input())
        M[i].append(N)

c = 0
s = 0
count = 0
for i in range(11,0,-1):

    c +=1
    for j in range(c, 12):

        s += M[i][j]
        count += 1

if(op == 'S'):

    print('{}'.format(s))

if(op == 'M'):

    med = s / count
    print('{:.1f}'.format(med))
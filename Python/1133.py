n1 = int(input())
n2 = int(input())
arr = [n1] + [n2]
arr.sort()

for i in range(arr[0] + 1, arr[1]):

    if(i % 5 == 2 or i % 5 == 3):

        print(i)
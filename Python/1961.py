p, n = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(1, n):

    if(abs(arr[i - 1] - arr[i]) > p):

        print("GAME OVER")
        break

    elif(i == n - 1):

        print("YOU WIN")
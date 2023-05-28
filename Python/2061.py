num, count = map(int, input().split())

for _ in range(count):

    act = input()

    if(act == "fechou"):

        num += 1

    else:

        num -= 1

print(num)
UM = input().split(" ")
DOIS = input().split(" ")

x1, y1 = UM
x2, y2 = DOIS

DIST = (((float(x2) - float(x1)) ** 2) + ((float(y2) - float(y1)) ** 2)) ** 0.5

print("{}".format("{:.4f}".format(DIST)))

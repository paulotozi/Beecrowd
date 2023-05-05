SEC = int(input())

HRS = SEC // 3600
SEC -= HRS * 3600

MIN = SEC // 60
SEC -= MIN * 60

print("{}:{}:{}".format(HRS, MIN, SEC))

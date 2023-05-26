p1, p2 = map(float, input().split())
diff = p2 - p1

print("{:.2f}%".format((diff / p1) * 100))
w, b, h = map(float, input().split())
result = (((w * b * h) / 8 ) / 1024 / 1024)
print("{:.2f} MB".format(result))
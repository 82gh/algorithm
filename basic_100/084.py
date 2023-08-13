h, b, c, s = map(float, input().split())
result = (((h * b * c * s) / 8) / 1024 ) / 1024
print("{:.1f} MB".format(result))
a, d, n = map(int, input().split())
cnt = 2
while cnt <= n:
    a += d
    cnt += 1
print(a)
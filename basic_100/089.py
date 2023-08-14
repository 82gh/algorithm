a, r, n = map(int, input().split())
cnt = 2

while cnt <= n:
    a *= r
    cnt += 1
print(a)
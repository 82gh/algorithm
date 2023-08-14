a, m, d, n = map(int, input().split())
cnt = 2
while cnt <= n:
    prevNum = a
    a = prevNum * m + d
    cnt += 1
print(a)


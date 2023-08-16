user_1, user_2, user_3 = map(int, input().split())
result = 1
while result % user_1 != 0 or result % user_2 != 0 or result % user_3 != 0:
    result += 1

print(result)

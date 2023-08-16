num = int(input())
call = list(map(int, input().split()))

for i in range(num-1, -1 , -1):
    print(call[i], end = " ")
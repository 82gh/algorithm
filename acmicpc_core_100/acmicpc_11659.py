import sys

input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
# partialSum = [0] * N
partialSum = [0]
temp = 0
for i in nums:
    temp = temp + i
    partialSum.append(temp)

print(partialSum)


for k in range(M):
    i, j = map(int, input().split())
    print(partialSum[j] - partialSum[i - 1])

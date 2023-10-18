import sys

input = sys.stdin.readline
N = int(input())
scoreList = list(map(int, input().split()))
maxScore = max(scoreList)
sum = sum(scoreList)
result = ((sum / maxScore) * 100 / N)
print(result)

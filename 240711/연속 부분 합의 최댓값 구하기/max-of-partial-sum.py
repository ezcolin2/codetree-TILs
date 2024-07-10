import sys
input = sys.stdin.readline
MIN_VALUE = -1001

n = int(input())
sequence = list(map(int, input().split()))

# dp[i] : 인덱스 i번 원소가 부분 수열의 마지막 원소일 때 부분 수열 합의 최대 값
dp = [MIN_VALUE for _ in range(n)]
dp[0] = sequence[0]

for i in range(1, n):
    dp[i] = max(dp[i], dp[i-1] + sequence[i], sequence[i])

print(max(dp))
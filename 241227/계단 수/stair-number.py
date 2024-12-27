n = int(input())
# dp[i][j] : 길이가 i일 때 마지막 숫자가 j인 계단 수의 개수
dp = [[0]*(10) for _ in range(n+1)]

dp[1][0] = 0
# 길이가 1일 때는 무조건 1
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j > 0:
            dp[i][j] += dp[i-1][j-1]
        if j < 9:
            dp[i][j] += dp[i-1][j+1]

print(sum(dp[-1])%1000000007)
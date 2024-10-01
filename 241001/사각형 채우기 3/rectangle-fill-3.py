import sys
input = sys.stdin.readline
n = int(input())
dp = [0]*(max(n+1, 4))
dp[0] = 1
dp[1] = 2
dp[2] = 7
dp[3] = 22
for i in range(4, n+1):
    dp[i] = dp[i-1]*dp[1] + dp[i-2]*3
    for j in range(0, i-2):
        dp[i] += dp[j]*2
print(dp[n]%1000000007)
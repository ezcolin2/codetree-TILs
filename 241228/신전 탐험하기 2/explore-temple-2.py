n = int(input())
treasures = [[0, 0, 0]]+[list(map(int, input().split())) for _ in range(n)]

# dp[i][j] : i층에서 j 방향의 방에 들어갔을 때 보물 최대 개수
dp = [[0]*3 for _ in range(n+1)]
for i in range(1, n+1):
    dp[i][0] = max(dp[i-1][1] + treasures[i][0], dp[i-1][2] + treasures[i][0])
    dp[i][1] = max(dp[i-1][0] + treasures[i][1], dp[i-1][2] + treasures[i][1])
    dp[i][2] = max(dp[i-1][0] + treasures[i][2], dp[i-1][1] + treasures[i][2])
print(max(dp[n]))
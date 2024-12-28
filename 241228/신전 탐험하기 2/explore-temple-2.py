n = int(input())
treasures = [[0, 0, 0]]+[list(map(int, input().split())) for _ in range(n)]
# dp[i][j][k] : i층에서 j 방향의 방에 들어갔을 때 1층에서 들어갔단 방향이 k일 때 보물 최대 개수
dp = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(n+1)]
for i in range(3):
    dp[1][i][i] = treasures[1][i]
for i in range(3):
    for j in range(3):
        if i==j:
            continue
        dp[2][i][j] = dp[1][j][j] + treasures[2][i]
for i in range(3, n+1):
    for j in range(3):
        dp[i][0][j] = max(dp[i-1][1][j] + treasures[i][0], dp[i-1][2][j] + treasures[i][0])
        dp[i][1][j] = max(dp[i-1][0][j] + treasures[i][1], dp[i-1][2][j] + treasures[i][1])
        dp[i][2][j] = max(dp[i-1][0][j] + treasures[i][2], dp[i-1][1][j] + treasures[i][2])
res = 0
for i in range(3):
    for j in range(3):
        if i == j:
            continue
        res = max(res, dp[n][i][j])
print(res)
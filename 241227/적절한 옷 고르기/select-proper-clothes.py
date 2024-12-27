n, m = map(int, input().split())
clothes = [tuple(map(int, input().split())) for _ in range(n)]
default_value = -1
# dp[i][j] : i일에 j번 옷을 입었을 때 최대 만족도
dp = [[default_value]*n for _ in range(m)]
for i in range(n):
    if clothes[i][0] > 1:
        continue
    dp[0][i] = 0
for i in range(m):
    for j in range(n):
        # 해당 날짜에 해당 옷을 입을 수 없다면 스킵
        if clothes[j][0]-1 > i or clothes[j][1]-1 < i:
            continue
        # 이전 날짜에 선택한 옷 고려
        for k in range(n):
            # 만약 default_value라면 불가능하므로 스킵
            if dp[i-1][k] == default_value:
                continue
            dp[i][j] = max(dp[i][j], dp[i-1][k] + abs(clothes[k][2]-clothes[j][2]))
print(max(dp[-1]))

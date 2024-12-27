n, m = map(int, input().split())
jewels = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]
# dp[i][j] : i번째 보석가지 고려했을 때 무게가 j이하일 때 최대 가치
dp = [[0]*(m+1) for _ in range(n+1)]

# 보석을 하나씩 늘려감
for i in range(1, n+1):
    weight, value = jewels[i]
    for j in range(1, m+1):
        # 무게를 넘어버리면 스킵
        if j < weight:
            continue
        
        # 1. 이전 무게 고려 
        # 2. 현재 보석을 선택하지 않을 때
        # 3. 현재 보석을 선택했을 때
        # 1, 2, 3번 중 가장 큰 값
        dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i-1][j-weight] + value)

print(dp[n][m])
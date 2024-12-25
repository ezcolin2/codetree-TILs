n, m = map(int, input().split())
backpacks = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]
# dp[i][j] : i번째 가방까지 고려한 상황에서 무게가 j이하일 때 최대 가치
dp = [0]*(m+1)

# 모든 무게에 대하여
for i in range(1, m+1):
    dp[i] = max(dp[i], dp[i-1])
    # 모든 보석을 하나씩 넣어봄
    for j in range(1, n+1):
        weight, value = backpacks[j]
        # 무게가 남을 때
        if i >= weight:
            dp[i] = max(dp[i], dp[i-weight] + value)
print(dp[m])
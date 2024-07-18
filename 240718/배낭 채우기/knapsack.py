import sys
input = sys.stdin.readline
# n : 보석의 개수
# m : 최대 무게
n, m = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(n)]

# weight[i] : 가치 i를 만들 때 최저 무게
weights = [sys.maxsize for _ in range(1000001)]
weights[0] = 0

# dp[i] : 무게의 합이 M이 넘지 않으면서 가치가 i개가 될 수 있는지
dp = [False for _ in range(1000001)]
dp[0] = True

# 보석들을 하나씩만 뽑을 수 있기 때문에 거꾸로
for w, v in jewels:
    for value in range(1000000, -1, -1):
        # 범위를 벗어나지 않으면서 가치를 만들 수 있으면서 무게가 넘지 않으면
        if value - v>=0 and dp[value-v] and weights[value-v] + w <= m:
            dp[value] = dp[value] or dp[value-v]
            weights[value] = min(weights[value], weights[value-v] + w) 

for i in range(1000000, -1, -1):
    if (dp[i]):
        print(i)
        break
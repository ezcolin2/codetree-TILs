import sys
MIN_VALUE = -sys.maxsize
n = int(input())
first_cards = list(map(int, input().split()))
second_cards = list(map(int, input().split()))

# dp[i][j] : 첫 번째 카드 더미의 가장 위가 i번째, 두 번째 카드 더미의 가장 위가 j번째 일 때 최대 점수
dp = [[MIN_VALUE]*(n+1) for _ in range(n+1)]
# 아직 게임을 하지 않았을 때
dp[0][0] = 0
for i in range(n+1):
    for j in range(n+1):
        if i == 0 and j == 0:
            continue
        # 남우가 져서 현재 상태가 되었을 때
        if j-1 >= 0 and i != n and first_cards[i] > second_cards[j-1]:
            dp[i][j] = max(dp[i][j], dp[i][j-1] + second_cards[j-1])
        # 남우가 이겨서 현재 상태가 되었을 때
        if i-1 >= 0 and j != n and first_cards[i-1] < second_cards[j]:
            dp[i][j] = max(dp[i][j], dp[i-1][j])
        # 비겨서 현재 상태가 되었을 때
        if i-1 >= 0 and j-1 >= 0 and first_cards[i-1] == second_cards[j-1]:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1])
        # 카드를 버렸을 때
        if i-1 >= 0 and j-1 >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1])
res = MIN_VALUE
for i in range(n+1):
    res = max(res, dp[n][i])
    res = max(res, dp[i][n])
print(res)
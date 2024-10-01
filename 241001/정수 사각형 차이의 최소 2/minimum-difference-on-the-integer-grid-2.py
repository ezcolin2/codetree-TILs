import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_dp = [row[:] for row in arr]
min_dp = [row[:] for row in arr]
# 일단 사이드의 확정된 것 부터 진행
for i in range(1, n):
    max_dp[i][0] = max(max_dp[i-1][0], max_dp[i][0])
    max_dp[0][i] = max(max_dp[0][i-1], max_dp[0][i])
    min_dp[i][0] = min(min_dp[i-1][0], min_dp[i][0])
    min_dp[0][i] = min(min_dp[0][i-1], min_dp[0][i])

# 시작
# 참고로 |최댓값 - 최솟값|이 최소가 되는 경로가 있으면 그 경로로 max_dp와 min_dp가 고정되어야 함
for i in range(1, n):
    for j in range(1, n):
        # 위에서 올 때
        up_difference = max(max_dp[i][j], max_dp[i-1][j]) - min(min_dp[i][j], min_dp[i-1][j])
        # 왼쪽에서 올 때
        left_difference = max(max_dp[i][j], max_dp[i][j-1]) - min(min_dp[i][j], min_dp[i][j-1])
        # 위에서 오는 게 더 낫다면
        if up_difference < left_difference:
            max_dp[i][j] = max(max_dp[i][j], max_dp[i-1][j])
            min_dp[i][j] = min(min_dp[i][j], min_dp[i-1][j])
        else:
            max_dp[i][j] = max(max_dp[i][j], max_dp[i][j-1])
            min_dp[i][j] = min(min_dp[i][j], min_dp[i][j-1]) 
print(max_dp[n-1][n-1] - min_dp[n-1][n-1])
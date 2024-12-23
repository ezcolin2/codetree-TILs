import sys
MAX_VALUE = sys.maxsize
def solve(arr, lower_bound):
    n = len(arr)
    max_dp = [row[:] for row in arr]
    # lower_bound보다 작으면 전부 무한대로
    for i in range(n):
        for j in range(n):
            if arr[i][j] < lower_bound:
                max_dp[i][j] = MAX_VALUE

    # 위쪽과 왼쪽 가장자리는 경로가 하나
    for i in range(1, n):
        max_dp[i][0] = max(max_dp[i-1][0], arr[i][0])
        max_dp[0][i] = max(max_dp[0][i-1], arr[0][i])
    
    # 시작
    for i in range(1, n):
        for j in range(1, n):
            if max_dp[i][j] == MAX_VALUE:
                continue
            max_dp[i][j] = min(max(arr[i][j], max_dp[i-1][j]), max(arr[i][j], max_dp[i][j-1]))
    return max_dp[n-1][n-1] - lower_bound

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = MAX_VALUE

for i in range(1, 101):
    res = min(res, solve(arr, i))
print(res)
import sys
input = sys.stdin.readline
MIN_VAL = -sys.maxsize

n = int(input())
stairs = [0]+list(map(int, input().split()))

# dp[i][j] : 인덱스 i 계단에 1 계단을 단위로 j번 올라왔을 때 동전 개수 최대 값
dp = [[MIN_VAL for _ in range(3)] for _ in range(n+1)]
dp[0][0] = 0

# i 계단을 올라왔을 때 
for i in range(1, n+1):
    # 1 계단을 j번 사용
    for j in range(3):
        # i 계단을 올라올 때 1계단 단위
        if j > 0 and dp[i-1][j-1] != MIN_VAL:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + stairs[i])

        # i 계단을 올라올 때 2계단 단위
        if i -2 >= 0 and dp[i-2][j] != MIN_VAL:
            dp[i][j] = max(dp[i][j], dp[i-2][j] + stairs[i])

print(max([max(row) for row in dp]))
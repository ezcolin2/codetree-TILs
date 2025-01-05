A = input()
B = input()

a_length = len(A)
b_length = len(B)

dp = [[0]*(b_length+1) for _ in range(a_length+1)]

# 초기화
for i in range(a_length+1):
    dp[i][0] = i
for j in range(b_length+1):
    dp[0][j] = j
for i in range(1, a_length+1):
    for j in range(1, b_length+1):
        # 같으면 그대로 
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            # 다르면 여러 연산 중 가장 적은 횟수
            dp[i][j] = min(dp[i-1][j]+1, dp[i-1][j-1]+1, dp[i][j-1]+1)
print(dp[-1][-1])

A = input()
B = input()

a_length = len(A)
b_length = len(B)

# dp 초기화
# dp[i][j]: A를 i번째까지 고려하고 B를 j번째까지 고려했을 때 최소 연산 횟수
dp = [[0]*(b_length+1) for _ in range(a_length+1)]
for i in range(a_length+1):
    dp[i][0] = i
for i in range(b_length+1):
    dp[0][i] = i

for i in range(1, a_length+1):
    for j in range(1, b_length+1):
        # 만약 끝이 같다면 그대로
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1]
        # 다르다면 연산 진행 후 작은 값
        else:
            # 1. 끝에 문자를 삽입
            # 2. 끝 문자를 제거
            dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1)

print(dp[-1][-1])
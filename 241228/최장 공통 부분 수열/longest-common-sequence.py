first_string = input()
second_string = input()
dp = [[0]*len(second_string) for _ in range(len(first_string))]

# 초기 값 세팅
if first_string[0] == second_string[0]:
    dp[0][0] = 1
else:
    dp[0][0] = 0

for i in range(1, len(first_string)):
    # 같다면 1
    if first_string[i] == second_string[0]:
        dp[i][0] = 1
    # 다르다면 그대로
    else:
        dp[i][0] = dp[i-1][0]

for i in range(1, len(second_string)):
    # 같다면 1
    if second_string[i] == first_string[0]:
        dp[0][i] = 1
    # 다르다면 그대로
    else:
        dp[0][i] = dp[0][i-1] 

for i in range(1, len(first_string)):
    for j in range(1, len(second_string)):
        # 같으면 1 증가
        if first_string[i] == second_string[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        # 다르다면
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            

print(dp[-1][-1])
        
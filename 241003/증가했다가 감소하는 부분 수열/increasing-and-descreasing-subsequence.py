n = int(input())
arr = list(map(int, input().split()))
# 오름차순
asc_dp = [1]*n
# 내림차순
desc_dp = [1]*n

# 오름차순 dp 구하기 
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            asc_dp[i] = max(asc_dp[i], asc_dp[j] + 1)

# 거꾸로 오르마순 dp 구하기
for i in range(n-2, 0, -1):
    for j in range(n-1, i-1, -1):
        if arr[i] > arr[j]:
            desc_dp[i] = max(desc_dp[i], desc_dp[j] + 1)

max_res = 0
for i in range(n-1):
    max_res = max(max_res, asc_dp[i] + desc_dp[i+1])
print(max_res)
import sys
n = int(input())
arr = list(map(int, input().split()))
# 하나의 그룹에서 만들 수 있는 합만 고려한다.
# 그러면 다른 그룹에서는 그 합을 빼기만 하면 된다.
# dp[i] : i번째 수까지 고려했을 때 만들 수 있는 합의 경우의 수
dp = [set() for _ in range(n)]
dp[0].add(arr[0])

for i in range(1, n):
    # 이전 합 순회
    for sum_value in dp[i-1]:
        # i번째 수를 더하지 않음
        dp[i].add(sum_value)
        dp[i].add(sum_value + arr[i])
total_sum = sum(arr)
res = sys.maxsize
for value in dp[-1]:
    res = min(res, abs(value - (total_sum-value)))
print(res)
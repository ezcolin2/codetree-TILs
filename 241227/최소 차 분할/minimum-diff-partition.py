n = int(input())
arr = list(map(int, input().split()))
# dp[i] : i번째 수까지 고려했을 때 두 그룹 간 차이가 가능한 모든 경우의 수
# 최소 값은 1000을 초과할 수 없기 때문에 1000이 넘는 경우는 고려하지 않는다.
# dp[i]는 set으로 구성하여 중복된 값이 없도록 한다.
# 공간 복잡도 : O(NM)
# 시간 복잡도 : O(NM)

# 모든 수를 순회하면서 이전에 나온 모든 값에 대해 덧셈, 뺄셈을 진행한다.
dp = [set() for _ in range(n)]
dp[0].add(arr[0])
for i in range(1, n):
    # 이전 값을 모두 순회한다.
    for value in dp[i-1]:
        dp[i].add(abs(value-arr[i]))
        if value+arr[i] > 1000:
            continue
        dp[i].add(value+arr[i])
print(min(dp[-1]))
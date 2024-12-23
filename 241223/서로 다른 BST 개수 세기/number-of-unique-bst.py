# n개의 노드로 만들 수 있는 서로 다른 BST의 개수 구하는 함수
def get_number_of_BST(dp, n):
    res = 0
    for i in range(n):
        res += dp[i] * dp[n-i-1]
    return res
dp = [0]*20
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 5

n = int(input())
# dp 초기화
for i in range(4, n+1):
    dp[i] = get_number_of_BST(dp, i)
print(dp[n])
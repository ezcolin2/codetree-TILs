import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 최상단에서 오른쪽으로만 갔을 때를 구함
for i in range(1, n):
    arr[0][i] += arr[0][i-1]

# 좌측에서 아래로만 갔을 때를 구함
for i in range(1, n):
    arr[i][0] += arr[i-1][0]

# 나머지를 구함 
for i in range(1, n):
    for j in range(1, n):
        arr[i][j] = max(arr[i][j] + arr[i-1][j], arr[i][j] + arr[i][j-1])
print(arr[n-1][n-1])
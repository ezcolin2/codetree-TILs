import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 최상단 우측
for i in range(1, n):
    arr[0][i] = min(arr[0][i], arr[0][i-1])

# 좌측 아래 
for i in range(1, n):
    arr[i][0] = min(arr[i][0], arr[i-1][0])

for i in range(1, n):
    for j in range(1, n):
        arr[i][j] = min(arr[i][j], max(arr[i-1][j], arr[i][j-1]))

print(arr[n-1][n-1])
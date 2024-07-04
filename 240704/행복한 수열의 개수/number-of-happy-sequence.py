import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
res = 0
for i in range(n):
    cnt = 1
    for j in range(n):
        if j>=1:
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
            else:
                cnt = 1
    if cnt>=m:
        res+=1
for j in range(n):
    cnt = 1
    for i in range(n):
        if i>=1:
            if arr[i][j] == arr[i-1][j]:
                cnt += 1
            else:
                cnt = 1
    if cnt>=m:
        res+=1
print(res)
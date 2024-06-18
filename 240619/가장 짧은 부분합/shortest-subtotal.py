import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))

# 가장 짧은 구간의 길이
res = 100000
# two pointer
for i in range(n):
    sum_val = 0
    for j in range(i, n):
        sum_val += arr[j]
        # 처음으로 s가 넘으면 시작점이 i인 곳의 가장 짧은 길이를 구한 것이기 때문에 break
        if sum_val >= s:
            res = min(res, j-i+1)
            break
print(res)
import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))

# 가장 짧은 구간의 길이
res = 100000

# 합
sum_val = 0
j = 0
# two pointer
for i in range(n):
    while j < n and sum_val < s:
        # 더함
        sum_val += arr[j]
        j += 1
    if sum_val < s:
        break
    res = min(res, j-i)
    sum_val -= arr[i]
print(res)
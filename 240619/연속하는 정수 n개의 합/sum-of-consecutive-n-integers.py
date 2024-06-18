import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
# 합
sum_val = 0
j = 0

# 경우의 수
cnt = 0
for i in range(n):
    while (j < n and sum_val + arr[j] <= m):
        sum_val += arr[j]
        j+=1
    # m이 되면 경우의 수 증가
    if sum_val == m:
        cnt+=1
    sum_val -= arr[i]
print(cnt)
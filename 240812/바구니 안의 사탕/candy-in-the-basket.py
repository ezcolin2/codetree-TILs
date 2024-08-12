import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]

# 바구나 좌표를 기준으로 오름차순 정렬
arr.sort(key = lambda x : x[1])

# 누적 합의 범위는 사탕이 들어있는 마지막 바구니의 위치
# 1부터 시작하므로 1 추가
prefix_sum = [0 for _ in range(arr[-1][1] + 1)]

# arr를 순회하면서 해당 위치에 사탕 개수 추가
for candy, location in arr:
    prefix_sum[location] = candy

# 누적 합 구함
for i in range(1, len(prefix_sum)):
    prefix_sum[i] += prefix_sum[i-1]

# 2*k 범위에 해당하는 곳의 합을 구함
max_val = 0
for i in range(2*k, len(prefix_sum)):
    max_val = max(max_val, prefix_sum[i] - prefix_sum[i-2*k-1])
print(max_val)
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
squares = [list(map(int, input().split())) for _ in range(k)]

# 순서대로 a, b, c의 누적 합
prefix_sum = [[[0 for _ in range(m+1)] for _ in range(n+1)] for _ in range(3)]

# 누적합 구하기
alphabets = ['a', 'b', 'c']
for i in range(1, n+1):
    for j in range(1, m+1):
        # 'a', 'b', 'c'에 대한 누적합 구하기
        for alphabet in alphabets:
            idx = ord(alphabet) - ord('a')
            prefix_sum[idx][i][j] += prefix_sum[idx][i-1][j] + prefix_sum[idx][i][j-1] - prefix_sum[idx][i-1][j-1]
            if arr[i-1][j-1] == alphabet:
                prefix_sum[idx][i][j] += 1

# 범위 누적합 구하는 함수
def get_range_sum(r1, c1, r2, c2, idx):
    return prefix_sum[idx][r2][c2] - prefix_sum[idx][r2][c1-1] - prefix_sum[idx][r1-1][c2] + prefix_sum[idx][r1-1][c1-1]

for r1, c1, r2, c2 in squares:
    print(get_range_sum(r1, c1, r2, c2, 0), get_range_sum(r1, c1, r2, c2, 1),get_range_sum(r1, c1, r2, c2, 2))
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[0]*(m+1)] + [ [0]+list(map(int, input().split())) for _ in range(n)]
# 음수 개수 누적합 구하기
def get_prefix_sum(arr):
    prefix_sum = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 음수면 개수 1
            if arr[i][j] < 0:
                prefix_sum[i][j] = 1
            # 누적합 구하기
            prefix_sum[i][j] += prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]
    return prefix_sum

# 가능한 사각형인지
def is_possible_square(n, m, start_x, start_y, end_x, end_y):
    return (
        1<=start_x<=n and
        1<=start_y<=m and
        1<=end_x<=n and
        1<=end_y<=m and
        start_x <= end_x and
        start_y <= end_y
    )
# 양수 직사각형인지
def is_plus_square(prefix_sum, start_x, start_y, end_x, end_y):
    minus_cnt = prefix_sum[end_x][end_y] - prefix_sum[start_x-1][end_y] - prefix_sum[end_x][start_y-1] + prefix_sum[start_x-1][start_y-1]
    return minus_cnt == 0

# 최대 크기 양수 직사각형
def get_max_size(arr):
    n = len(arr) - 1
    m = len(arr[0]) - 1
    max_size = 0
    prefix_sum = get_prefix_sum(arr)
    # 모든 경우
    for start_x in range(1, n+1):
        for start_y in range(1, m+1):
            for end_x in range(1, n+1):
                for end_y in range(1, m+1):
                    # 불가능한 사각형이면 스킵
                    if not is_possible_square(
                        n, 
                        m, 
                        start_x,
                        start_y,
                        end_x,
                        end_y    
                    ):
                        continue
                    
                    # 양수 직사각형이 아니면 패스
                    if not is_plus_square(
                        prefix_sum,
                        start_x,
                        start_y,
                        end_x,
                        end_y
                    ):
                        continue
                    
                    
                    # 양수 직사각형이면 크기 갱신
                    max_size = max(max_size, (end_x-start_x+1) * (end_y-start_y+1))
    return max_size
res = get_max_size(arr)
if res == 0:
    print(-1)
    exit()
print(res)
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[0]*(n+1)] + [[0]+list(map(int, input().split())) for _ in range(n)]
# 누적합 구하기
def get_prefix_sum_arr(arr):
    prefix_sum = [row[:] for row in arr]
    n = len(arr)-1
    for i in range(1, n+1):
        for j in range(1, n+1):
            prefix_sum[i][j] += prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]
    return prefix_sum

# 특정 정사각형 내부 누적 합 구하기
def get_prefix_sum(prefix_sum_arr, row_start, row_end, col_start, col_end):
    return (
        prefix_sum_arr[row_end][col_end] - 
        prefix_sum_arr[row_end][col_start-1] - 
        prefix_sum_arr[row_start-1][col_end] + 
        prefix_sum_arr[row_start-1][col_start-1]
    )

# 정사각형 검증
def is_possible_square(row_start, col_start, row_end, col_end):
    return row_start<=row_end and col_start<=col_end

# 겹치는지
def is_overlapped(
    a_row_start, 
    a_row_end, 
    a_col_start, 
    a_col_end,
    b_row_start, 
    b_row_end, 
    b_col_start, 
    b_col_end,
):
    # if a_row_start <= b_row_start <= a_row_end:
    #     return True
    # if a_row_start <= b_row_end <= a_row_end:
    #     return True    
    # if a_col_start <= b_col_start <= a_col_end:
    #     return True
    # if a_col_start <= b_col_end <= a_col_end:
    #     return True    
    # return False
    if a_row_start > b_row_end:
        return False
    if a_row_end < b_row_start:
        return False
    if a_col_end < b_col_start:
        return False
    if a_col_start > b_col_end:
        return False
    return True
# arr 중 겹치지 않는 두 직사각형을 잡아 최대 합
def get_max_sum(arr):
    prefix_sum_arr = get_prefix_sum_arr(arr)
    max_sum = -sys.maxsize
    n = len(arr)-1
    for a_row_start_idx in range(1, n+1):
        for a_row_end_idx in range(a_row_start_idx, n+1):
            for a_col_start_idx in range(1, n+1):
                for a_col_end_idx in range(a_col_start_idx, n+1):
                    for b_row_start_idx in range(a_row_start_idx, n+1):
                        for b_row_end_idx in range(b_row_start_idx, n+1):
                            for b_col_start_idx in range(a_col_start_idx, n+1):
                                for b_col_end_idx in range(b_col_start_idx, n+1):
                                    if is_overlapped(
                                        a_row_start_idx,
                                        a_row_end_idx,
                                        a_col_start_idx,
                                        a_col_end_idx,
                                        b_row_start_idx,
                                        b_row_end_idx,
                                        b_col_start_idx,
                                        b_col_end_idx
                                    ):
                                        continue

                                    max_sum = max(
                                        max_sum, 
                                        get_prefix_sum(
                                            prefix_sum_arr, 
                                            a_row_start_idx, 
                                            a_row_end_idx, 
                                            a_col_start_idx,
                                            a_col_end_idx
                                            )+
                                        get_prefix_sum(
                                            prefix_sum_arr, 
                                            b_row_start_idx, 
                                            b_row_end_idx, 
                                            b_col_start_idx,
                                            b_col_end_idx
                                            )
                                        )
    return max_sum
print(get_max_sum(arr))
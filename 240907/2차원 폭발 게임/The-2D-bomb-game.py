import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 폭탄을 터뜨리는 함수
# m개 이상 연속된 폭탄을 터뜨리는 경우
# 1. 연속된 폭탄이 m개 이상 나오다가 숫자가 다른 폭탄이 나왔을 때
# 2. 순회가 끝났을 경우
def explode(arr, m):
    n = len(arr)
    new_arr = [row[:] for row in arr]
    for col_idx in range(n):
        start_idx, end_idx = 0, 0 # l, r
        while True:
            # 반복문 처음 시작한다는 것은 start_idx ~ end_idx까지 연속된다는 뜻
            # 마지막이라면 종료
            if end_idx == n-1:
                # 연속 횟수 체크해서 터뜨림
                if end_idx - start_idx + 1 >= m:
                    for i in range(start_idx, end_idx+1):
                        new_arr[i][col_idx] = 0
                break
            # 다른 게 나왔다면
            if arr[start_idx][col_idx] != arr[end_idx+1][col_idx]:
                # 연속 횟수 체크해서 터뜨림
                if end_idx - start_idx + 1 >= m:
                    for i in range(start_idx, end_idx+1):
                        new_arr[i][col_idx] = 0
                start_idx = end_idx+1
                end_idx = end_idx+1
                continue
            # 같은 게 나왔다면
            end_idx += 1
        
    return new_arr
# 중력 적용
def fall(arr):
    n = len(arr)
    new_arr = [[0]*n for _ in range(n)]
    for col_idx in range(n):
        # 0인 것을 제외하고 순서대로 쌓는다.
        new_row_idx = n-1
        for row_idx in range(n-1, -1, -1):
            # 0인 것은 패스
            if arr[row_idx][col_idx] == 0:
                continue
            # 0이 아니라면 
            new_arr[new_row_idx][col_idx] = arr[row_idx][col_idx]
            new_row_idx -= 1
    return new_arr

def rotate(arr):
    n = len(arr)
    new_arr = [[0]*n for _ in range(n)]
    for row_idx in range(n):
        for col_idx in range(n):
            new_arr[col_idx][n-1-row_idx] = arr[row_idx][col_idx]
    return new_arr

# 남은 폭탄 개수
def get_bomb_cnt(arr):
    n = len(arr)
    return n**2 - sum([row.count(0) for row in arr])    

# 터질 폭탄이 남아있는지
def is_bomb_remaining(arr, m):
    n = len(arr)
    new_arr = explode(arr, m)
    for i in range(n):
        for j in range(n):
            if arr[i][j]!=new_arr[i][j]:
                return True
    return False

def solution(arr, m, k):
    new_arr = [row[:] for row in arr]
    n = len(arr)
    for _ in range(k):
        # 터뜨림
        new_arr = explode(new_arr, m)
        # 떨어뜨림
        new_arr = fall(new_arr)
            # 끝나고도 터질 폭탄이 남아있다면
        while is_bomb_remaining(new_arr, m):
        # 터뜨림
            new_arr = explode(new_arr, m)
        # 떨어뜨림
            new_arr = fall(new_arr)
        # 회전
        new_arr = rotate(new_arr)

        # 떨어뜨림
        new_arr = fall(new_arr)
    while is_bomb_remaining(new_arr, m):
        # 터뜨림
        new_arr = explode(new_arr, m)
        # 떨어뜨림
        new_arr = fall(new_arr)
    return new_arr
res_arr = solution(arr, m, k)
res = get_bomb_cnt(res_arr)
print(res)
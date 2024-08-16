import sys
input = sys.stdin.readline
# 상수
# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

m, n = map(int, input().split())
number_arr = [list(map(int, input().split())) for _ in range(m)]
color_arr = [list(map(int, input().split())) for _ in range(m)]

# 색칠되어 있는 모든 좌표 구하기
def get_color_locations(color_arr):
    # 좌표 배열
    res = []
    for row_idx, row in enumerate(color_arr):
        for col_idx, col in enumerate(row):
            # 색칠되어 있다면 해당 좌표 배열에 추가
            if col == 1:
                res.append((row_idx, col_idx))
    return res

    
# 차이가 D 이하로 차이나느 칸으로만 이동하고 방문 배열을 반환
def bfs(start, d, number_arr):
    # 방문 배열 생성
    visited = [[False] * len(number_arr[0]) for _ in range(len(number_arr))]
    
    # 큐 생성
    queue = [start]
    
    # 큐가 빌 때까지 반복
    while queue:
        x, y  = queue.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 이동 가능하면 큐에 넣음
            if (
                0 <= nx < len(number_arr) and 
                0 <= ny < len(number_arr[0]) and 
                not visited[nx][ny] and 
                abs(number_arr[x][y] - number_arr[nx][ny]) <= d
            ):
                queue.append((nx, ny))
                visited[nx][ny] = True
    return visited

# d 이하로 차이나는 칸으로만 이동해서 색칠된 칸끼리 이동이 가능한지
def is_possible(number_arr, color_arr, d):
    # 색칠된 칸의 좌표를 모두 구한다.
    color_locations = get_color_locations(color_arr)
    
    # 색칠된 칸의 좌표 중 첫 번째를 시작점으로 해서 탐색을 진행한다.
    visited_arr = bfs(color_locations[0], d, number_arr)

    # 색칠된 칸을 모두 방문했는지 확인한다.
    for x, y in color_locations:
        # 색칠ㄹ된 칸 중 하나라도 방문하지 않았다면 False 반환
        if not visited_arr[x][y]:
            return False
    return True

# 이진 탐색
def parametric_search(number_arr, color_arr):
    min_res = sys.maxsize
    left, right = 0, 1000000000
    while left <= right:
        mid = (left + right)//2
        # 이동이 가능하다면 더 작은 숫자도 가능한지 확인
        if is_possible(number_arr, color_arr, mid):
            right = mid-1
            min_res = min(min_res, mid)
        else:
            left = mid+1
    return min_res
print(parametric_search(number_arr, color_arr))
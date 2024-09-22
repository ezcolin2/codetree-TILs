from collections import deque
import sys
INF = sys.maxsize
# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 모든 지점 활성화 여부 
def is_possible(arr):
    n = len(arr)
    start_x, start_y = -1, -1
    # 시작 지점 찾기
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                start_x, start_y = i, j
    
    # 방문하기
    visited = [[False]*n for _ in range(n)]
    queue = deque([(start_x, start_y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and arr[nx][ny] != -1:
                queue.append((nx, ny))
                visited[nx][ny] = True
    
    # 모두 활성화 시켰는지
    for i in range(n):
        for j in range(n):
            # 활성화 되지 않은 곳인데 방문하지 않았다면
            if arr[i][j] == 2 and not visited[i][j]:
                return False
    return True
    
# 시작 점에서 다른 활성화 지점까지 걸리는 시간 중 최소 값 반환
# 이 함수의 의미는 [start_x][start_y]까지 도달하는데 걸리는 최소 시간
def get_min_distance(arr, start_x, start_y):
    min_distance = INF
    n = len(arr)
    visited = [[False]*n for _ in range(n)]
    queue = deque([(start_x, start_y, 0)])
    visited[start_x][start_y] = True
    # bfs 시작
    while queue:
        x, y, distance = queue.popleft()
        # 만약 뽑은 곳이 활성화 혹은 활성화 되지 않은 지점이라면 갱신
        if not (x == start_x and y == start_y) and (arr[x][y] == 1 or arr[x][y] == 2):
            min_distance = min(min_distance, distance)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 범위를 벗어나지 않았다면
            # 아직 방문하지 않았다면
            # 갈 수 있다면 
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and arr[nx][ny]!=-1:
                queue.append((nx, ny, distance + 1))
                visited[nx][ny] = True
    return min_distance

def solution(arr):
    total_distance = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            # 활성화되지 않은 지점이라면
            if arr[i][j] == 2:
                # 이 지점까지 도착하는데 걸리는 최소 시간을 구해서 더함
                total_distance += get_min_distance(arr, i, j)
    return total_distance
if not is_possible(arr):
    print(-1)
    exit()
print(solution(arr))
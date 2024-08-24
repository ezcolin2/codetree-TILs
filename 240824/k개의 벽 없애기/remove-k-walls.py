import sys
from collections import deque
input = sys.stdin.readline

# n : 격자의 크기 n x n
# k : 벽의 개수
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
start_x, start_y = list(map(lambda x:int(x)-1, input().split())) #  출발 좌표
end_x, end_y = list(map(lambda x:int(x)-1, input().split())) # 도착 좌표

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 방문 여부
visited = [[False for _ in range(n)] for _ in range(n)]

# 갈 수 있는지
def can_go(x, y):
    return 0<=x<n and 0<=y<n and not visited[x][y] and arr[x][y] == 0

# (x, y부터 시작해서 bfs 탐색
def bfs(start_x, start_y, end_x, end_y):
    # 걸린 시간을 담을 배열
    temp_arr = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
    queue = [(start_x, start_y)]
    visited[start_x][start_y] = True
    while queue:
        x, y = queue.pop()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]    
            if can_go(nx, ny):
                visited[nx][ny] = True
                queue.append((nx, ny))
                temp_arr[nx][ny] = temp_arr[x][y] + 1
    return temp_arr[end_x][end_y]

# 벽의 좌표 구함
walls = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            walls.append((i, j))
min_time = sys.maxsize
# 없앨 벽 k개 선택
def choose(idx, cnt):
    global start_x, start_y, end_x, end_y, walls, min_time
    if idx == len(walls):
        if cnt == k:
            res = bfs(start_x, start_y, end_x, end_y)
            # 0이 아닐 때만
            if res!=0:
                min_time = min(min_time, res)
        return
    # 없앨 벽 선택
    x, y = walls[idx]
    arr[x][y] = 0
    choose(idx+1, cnt+1)
    arr[x][y] = 1

    # 이 벽 선택 안 함
    choose(idx+1, cnt)
choose(0, 0)
if min_time == sys.maxsize:
    print(-1)
else:
    print(min_time)
from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def bfs(arr):
    n = len(arr)
    queue = deque()
    # 방문 여부
    visited = [[False]*n for _ in range(n)]
    min_distance = [[0]*n for _ in range(n)]
    # 상한 귤들을 큐에 넣어둔다.
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                queue.append((i, j))
                visited[i][j] = True

    # 탐색 시작
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and arr[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                min_distance[nx][ny] = min_distance[x][y] + 1
    
    return min_distance

def get_res_arr(arr, min_distance):
    n = len(arr)
    new_arr = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                new_arr[i][j] = -1
            # 귤이 있는데 상하지 않았다면 
            elif arr[i][j] == 1 and min_distance[i][j] == 0:
                new_arr[i][j] = -2
            # 귤이 있는데 상했다면
            elif arr[i][j] == 1 and min_distance[i][j] > 0:
                new_arr[i][j] = min_distance[i][j]
            # 상한 귤이라면 0
            # 끝까지 상하지 않았다면
            
    return new_arr

min_distance = bfs(arr)
res_arr = get_res_arr(arr, min_distance)
for row in res_arr:
    for val in row:
        print(val, end=' ')
    print()
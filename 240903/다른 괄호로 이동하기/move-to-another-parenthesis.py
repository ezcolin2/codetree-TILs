import heapq
import sys
INF = sys.maxsize
n, a, b = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]

# 동서남북 
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

#graph[i][j]의 뜻 : (i, j) 좌표에 존재하는 정점과 연결된 정점 (동서남북)
graph = [[[] for _ in range(n)] for _ in range(n)]

# 모든 arr를 돌면서 graph 매핑
for i in range(n):
    for j in range(n):
        for k in range(4):
            nx, ny = i+dx[k], j+dy[k]
            # 좌표를 벗어나지 않는다면
            if 0<=nx<n and 0<=ny<n:
                # 같으면 가중치 a, 다르면 가중치 b
                graph[i][j].append((a, nx, ny) if arr[i][j] == arr[nx][ny] else (b, nx, ny))

# 최소 거리
def djikstra(start_x, start_y):
    dist = [[INF]*n for _ in range(n)]
    dist[start_x][start_y] = 0
    queue = [(dist[start_x][start_y], start_x, start_y)]
    while queue:
        distance, x, y = heapq.heappop(queue)
        if dist[x][y] != distance:
            continue
        # 정점에 연결된 모든 정점들의 거리 값 갱신
        for temp_dist, temp_x, temp_y in graph[x][y]:
            if dist[temp_x][temp_y] > distance + temp_dist:
                dist[temp_x][temp_y] = distance + temp_dist
                queue.append((dist[temp_x][temp_y], temp_x, temp_y))

    # (start_x, start_y)로부터 다른 좌표까지의 최대 값 구하기
    res = 0
    for i in range(n):
        for j in range(n):
            res = max(res, dist[i][j])
    return res

# 모든 점에 대해서 다익스트라 실행
result = 0
for i in range(n):
    for j in range(n):
        result = max(result, djikstra(i, j))
print(result)
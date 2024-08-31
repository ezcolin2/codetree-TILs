import sys
input = sys.stdin.readline
INF = sys.maxsize
n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
dist = [INF]*(n+1)
visited = [False] * (n+1)
for _ in range(m):
    a, b, weight = map(int, input().split())
    graph[a][b] = weight

dist[1] = 0
for i in range(1, n+1):

    # 연결된 간선들 중 가장 낮은 가중치 구하기
    min_idx = -1
    for j in range(1, n+1):
        if visited[j]:
            continue
        if min_idx == -1 or dist[min_idx] > dist[j]:
            min_idx = j

    visited[min_idx] = True

    for j in range(1, n+1):
        if graph[min_idx][j] == 0:
            continue
        dist[j] = min(dist[j], dist[min_idx] + graph[min_idx][j])

for i in range(2, n+1):
    print(dist[i] if dist[i] != INF else -1)
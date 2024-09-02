import sys
input = sys.stdin.readline
INF = sys.maxsize
n, m = map(int, input().split())
v1, v2, e = map(int, input().split())
# 최소 거리 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 0
for _ in range(m):
    a, b, weight = map(int, input().split())
    graph[a][b] = weight
    graph[b][a] = weight

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

res = graph[v1][e] + graph[v2][e]
# 경유하는 점 찾기 
for i in range(1, n+1):
    res = min(res, graph[v1][i] + graph[v2][i] + graph[i][e])
print(res if res < INF else -1)
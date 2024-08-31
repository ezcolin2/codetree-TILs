import sys
input = sys.stdin.readline

INF = sys.maxsize
n, m = map(int, input().split())
dist = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dist[i][i] = 0

for _ in range(m):
    a, b, weight = map(int, input().split())
    dist[a][b] = min(dist[a][b], weight)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(dist[i][j] if dist[i][j] != INF else -1, end = ' ')
    print()
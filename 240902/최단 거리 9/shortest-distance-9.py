import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
dist = [INF]*(n+1)
path = [-1]*(n+1)

for _ in range(m):
    a, b, weight = map(int, input().split())
    graph[a].append((weight, b))
    graph[b].append((weight, a))

# a부터 시작해서 최단 거리, 경로 구하기
a, b = map(int, input().split())
dist[a] = 0
queue = [(dist[a], a)]

# 다익스트라 알고리즘 적용
while queue:
    val, v = heapq.heappop(queue)
    if val != dist[v]:
        continue
    # 연결된 정점 거리 갱신
    for new_val, new_v in graph[v]:
        if dist[new_v] > dist[v] + new_val:
            dist[new_v] = dist[v] + new_val
            path[new_v] = v
            queue.append((dist[new_v], new_v))

# 거꾸로 도착 지점까지 도착할 때까지
res = []
print(dist[b])
while b!= a:
    res.append(b)
    b = path[b]
res.append(a)
res.reverse()
for i in res:
    print(i, end=' ')
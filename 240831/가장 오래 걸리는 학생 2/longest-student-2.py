import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
dist = [INF]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, weight = map(int, input().split())
    # 가중치를 거꾸로 부여한다.
    graph[b].append((weight, a))
# 세팅
dist[n] = 0
queue = [(dist[n], n)]

# 다익스트라 알고리즘
while queue:
    weight, number = heapq.heappop(queue)
    if weight != dist[number]:
        continue

    # 정점을 골랐으니 연결된 모든 정점 최소 거리 갱신
    for w, v in graph[number]:
        if dist[v] > dist[number] + w:
            dist[v] = dist[number] + w
            heapq.heappush(queue, (dist[v], v))

max_res = 0
for i in range(1, n+1):
    if dist[i]!=INF and max_res < dist[i]:
        max_res = dist[i]
print(max_res)
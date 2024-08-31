import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize
n, m = map(int, input().split())
k = int(input())
graph = [[] for _ in range(n+1)]
dist = [INF]*(n+1)
for _ in range(m):
    a, b, weight = map(int, input().split())
    graph[a].append((b, weight))
    graph[b].append((a, weight))

# 다익스트라 알고리즘 시작
dist[k] = 0
queue = [(0, k)]

while queue:
    # 가장 작은 가중치를 지는 정점 가져오기
    weight, number = heapq.heappop(queue)
    if weight != dist[number]:
        continue

    # 해당 정점 기준으로 연결된 모든 정점 최소 거리 갱신
    current_weight = dist[number]
    for new_number, new_weight in graph[number]:
        if dist[new_number] > current_weight + new_weight:
            dist[new_number] = current_weight + new_weight
            heapq.heappush(queue, (dist[new_number], new_number))

for i in range(1, n+1):
    print(dist[i])
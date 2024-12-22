import sys
import heapq
INF = sys.maxsize
# start로부터 나머지 점까지의 최단 거리 구하기
def djikstra(start, graph):
    distances = [INF]*len(graph)
    distances[start] = 0

    # 최소 힙
    queue = [(distances[start], start)]
    while queue:
        # 저장된 값과 다르면 스킵
        current_distance, current_number = heapq.heappop(queue)
        if current_distance != distances[current_number]:
            continue
        
        # 연결된 모든 거리 갱신
        for next_distance, next_number in graph[current_number]:
            if distances[next_number] > current_distance + next_distance:
                distances[next_number] = current_distance + next_distance
                heapq.heappush(queue, (distances[next_number], next_number))
    return distances

n, m = map(int, input().split())
a, b, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    temp_a, temp_b, distance = map(int, input().split())
    graph[temp_a].append((distance, temp_b))
    graph[temp_b].append((distance, temp_a))

# a, b, c 각 점을 출발점으로 하는 최단 거리 구하기
min_distance_from_a = djikstra(a, graph)
min_distance_from_b = djikstra(b, graph)
min_distance_from_c = djikstra(c, graph)

# 결과 값
res = 0

for i in range(1, n+1):
    res = max(res, min(
            min_distance_from_a[i], 
            min_distance_from_b[i], 
            min_distance_from_c[i]
        ))
print(res)
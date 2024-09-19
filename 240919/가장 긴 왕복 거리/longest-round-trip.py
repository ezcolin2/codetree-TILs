import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize
n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
reverse_graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, distance = map(int, input().split())
    graph[a].append((distance, b))
    reverse_graph[b].append((distance, a))

# graph의 start 점으로부터 다른 모든 점에 대해서 최단 거리 배열 구하기
def get_distance_arr(graph, start):
    n = len(graph) - 1
    dist = [INF]*(n+1)
    dist[start] = 0
    # 우선순위 큐
    queue = [(0, start)]
    while queue:
        # 최단거리가 확정된 점을 꺼낸다.
        min_distance, min_node = heapq.heappop(queue)
        # 다른 값이 있으면 패스
        if dist[min_node] != min_distance:
            continue
        # 이 점과 연결된 다른 모든 점에 대해서 최단 거리를 갱신한다.
        for next_distance, next_node in graph[min_node]:
            # 갱신
            if dist[next_node] > min_distance + next_distance:
                dist[next_node] = min_distance + next_distance
                heapq.heappush(queue, (dist[next_node], next_node))
            
    return dist

# 가장 긴 왕복 시간
def get_round_trip_time(graph, reverse_graph, start):
    n = len(graph)-1
    start_distance_arr = get_distance_arr(graph, start)
    end_distance_arr = get_distance_arr(reverse_graph, start)
    max_time = 0
    for i in range(1, n+1):
        max_time = max(max_time, start_distance_arr[i] + end_distance_arr[i])
    return max_time

print(get_round_trip_time(graph, reverse_graph, x))
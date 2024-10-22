import sys
import heapq
INF = sys.maxsize

# 다익스트라 시작
def djikstra(graph, start):
    n = len(graph)-1
    distance = [INF]*(n+1)
    # 초기 값 
    distance[start] = 0
    queue = [(distance[start], start)]

    # 순회 시작
    while queue:
        # 확정된 최단 거리
        curr_distance, curr_node = heapq.heappop(queue)
        if distance[curr_node] != curr_distance:
            continue
        # 연결된 모든 정점에 대해 최단 거리 갱신
        for next_node in range(1, n+1):
            if graph[curr_node][next_node] == 0:
                continue
            next_distance = graph[curr_node][next_node]
            if distance[next_node] > curr_distance + next_distance:
                distance[next_node] = curr_distance + next_distance
                # 큐에 넣어줌
                heapq.heappush(queue,(distance[next_node], next_node))
    return distance

# start 점에서 end 갈 때 사전 순으로 가장 앞선 최단 거리 경로를 구한다.
def get_min_distance_path(graph, distance, start, end):
    n = len(graph)-1
    # 거꾸로 구한다.
    curr_node = start
    path = [curr_node]
    while curr_node != end:
        # 작은 것부터 조사
        for temp_node in range(1, n+1):
            if graph[curr_node][temp_node] == 0:
                continue
            if distance[temp_node]+graph[curr_node][temp_node] == distance[curr_node]:
                path.append(temp_node)
                curr_node = temp_node
                break
    return path
n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, distance = map(int, input().split())
    graph[a][b] = distance
    graph[b][a] = distance
a, b = map(int, input().split())
# 도착 점에서 출발했을 때의 최단 거리를 구한다.
distance = djikstra(graph, b)
origin_distance = djikstra(graph, a)
path = get_min_distance_path(graph, distance, a, b)
print(origin_distance[b])
for i in path:
    print(i, end=' ')
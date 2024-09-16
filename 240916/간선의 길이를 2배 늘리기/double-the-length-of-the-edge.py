import sys
import heapq
import copy
input = sys.stdin.readline
INF = sys.maxsize
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    i, j, d = map(int, input().split())
    graph[i].append([d, j])
    graph[j].append([d, i])

def find_min_path(graph, start, end):
    n = len(graph)-1
    # 우선순위 큐
    queue = []
    # 최단 경로
    path = [0 for _ in range(n+1)]
    # 최단 거리
    distance = 0 
    dist = [INF]*(n+1)
    dist[start] = 0
    heapq.heappush(queue, (0, start, 0))

    # 최단 거리 구하기
    while queue:
        min_distance, min_node, prev_node = heapq.heappop(queue)
        # 값이 갱신되었다면 패스
        if dist[min_node] != min_distance:
            continue
        # 아래 코드가 실행된다는 뜻은 다음 방문할 노드가 min_node라는 것이 확정
        # 거리 증가하고 경로에 추가
        distance += min_distance
        path[min_node] = prev_node
        # 연결된 모든 노드에 대해서 최단 거리 갱신
        for temp_distance, temp_node in graph[min_node]:
            if dist[temp_node] > dist[min_node] + temp_distance:
                dist[temp_node] = dist[min_node] + temp_distance
                heapq.heappush(queue, (dist[temp_node], temp_node, min_node))
    
    # 경로를 찾는다.
    res_path = []
    current_node = end
    while current_node != start:
        res_path.append(current_node)
        current_node = path[current_node]
    res_path.append(start)
    return res_path
# 그래프, 시작 점, 도착 점이 주어지면 최단 거리 반환
def find_min_distance(graph, start, end):
    n = len(graph)-1
    # 우선순위 큐
    queue = []
    # 최단 거리
    distance = 0 
    dist = [INF]*(n+1)
    dist[start] = 0
    heapq.heappush(queue, (0, start))

    # 최단 거리 구하기
    while queue:
        min_distance, min_node = heapq.heappop(queue)
        # 값이 갱신되었다면 패스
        if dist[min_node] != min_distance:
            continue
        # 아래 코드가 실행된다는 뜻은 다음 방문할 노드가 min_node라는 것이 확정
        # 거리 증가하고 경로에 추가
        distance += min_distance
        # 연결된 모든 노드에 대해서 최단 거리 갱신
        for temp_distance, temp_node in graph[min_node]:
            if dist[temp_node] > dist[min_node] + temp_distance:
                dist[temp_node] = dist[min_node] + temp_distance
                heapq.heappush(queue, (dist[temp_node], temp_node))

    return dist[end]
    
min_path = find_min_path(graph, 1, n)
origin_min_distance = find_min_distance(graph, 1, n)

# 간선의 길이를 두 배로 늘림
def make_edge_double(graph, start, end):
    new_graph = copy.deepcopy(graph)
    # 간선을 찾아서 두 배로 만듦
    for i in range(len(new_graph[start])):
        temp_distance, temp_node = new_graph[start][i]
        if temp_node == end:
            new_graph[start][i][0] *= 2
    for i in range(len(new_graph[end])):
        temp_distance, temp_node = new_graph[end][i]
        if temp_node == start:
            new_graph[end][i][0] *= 2        
    return new_graph

# 최단 거리들 중 최대 값
max_min_distance = 0
# 최단 경로의 모든 간선에 대해서 한 번씩 두 배로 만든 후 최단 거리를 구한다.
for i in range(1, len(min_path)):
    temp_graph = make_edge_double(graph, min_path[i], min_path[i-1])
    temp_min_distance = find_min_distance(temp_graph, 1, n)
    max_min_distance = max(max_min_distance, temp_min_distance)
print(abs(max_min_distance - origin_min_distance))
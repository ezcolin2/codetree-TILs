import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize
n, m = map(int, input().split())
red_a, red_b = map(int, input().split())

# 연결 리스트 그래프
graph = [[] for _ in range(n+1)]

# 그래프 생성
for _ in range(m):
    a, b, distance = map(int, input().split())
    graph[a].append((distance, b))
    graph[b].append((distance, a))

# 다익스트라
def djikstra(start, graph):
    # 최소 거리
    dist = [INF]*(n+1)
    
    # 시작 점부터 시작
    dist[start] = 0
    
    # 우선순위 큐
    # 거리가 가장 짧은 점을 고르기 위해 distance를 앞에 배치한다.
    queue = [(dist[start], start)]
    
    while queue:
        temp_distance, temp_start = heapq.heappop(queue)
        # 만약 값이 변경되었다면 패스한다.
        if temp_distance != dist[temp_start]:
            continue
        # 현재 가장 짧은 거리의 점과 연결된 모든 최단 거리를 갱신한다.
        for next_distance, next_vertex in graph[temp_start]:
            if dist[temp_start] + next_distance < dist[next_vertex]:
                dist[next_vertex] = dist[temp_start] + next_distance 
                # 갱신하면 우선순위 큐에 넣는다.
                heapq.heappush(queue, (dist[next_vertex], next_vertex))
    return dist

# start에서 시작하여 두 개의 빨간 점을 돌고 다시 시작 점으로 돌아오는 최단 거리
def get_min_distance(dist_from_red_a, dist_from_red_b, red_a, red_b, start):
    return dist_from_red_a[start] + dist_from_red_b[start] + dist_from_red_a[red_b]

# 최단 거리를 찾음
def find_min_distance(n, m, red_a, red_b, graph):
    # 시작점에서 빨간점의 거리를 구하는 것보다 빨간점에서 다른 모든 점에서 구하는 게 효울적
    dist_from_red_a = djikstra(red_a, graph)
    dist_from_red_b = djikstra(red_b, graph)

    
    # 최단 거리
    min_distance = INF
    # 시작 점을 하나씩 대입 
    for i in range(1, n+1):
        # 빨간 점 스킵
        if i == red_a or i == red_b:
            continue
        temp_min_distance = get_min_distance(dist_from_red_a, dist_from_red_b, red_a, red_b, i)
        min_distance = min(min_distance, temp_min_distance)
    return min_distance

print(find_min_distance(n, m, red_a, red_b, graph))
import sys
import heapq
INF = sys.maxsize
n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, distance = map(int, input().split())
    arr[a].append((distance, b))
    arr[b].append((distance, a))
a, b = map(int, input().split())

# 거리 배열
distance_arr = [INF]*(n+1)

# 처음 위치 0으로 초기화
distance_arr[a] = 0
queue = [(distance_arr[a], a)]

# 다익스트라 시작
while queue:
    # 가장 거리가 짧은 값 가져온다.
    distance, node = heapq.heappop(queue)

    # 만약 최신 값이 아니면 스킵 
    if distance_arr[node] != distance:
        continue
    
    # 이 위치로부터 갈 수 있는 모든 노드에 대해 최단 거리 갱신
    for next_distance, next_node in arr[node]:
        # 만약 최단 거리를 갱신할 수 있다면 갱신 후 큐에 넣기
        if distance_arr[next_node] > distance + next_distance:
            distance_arr[next_node] = distance + next_distance
            heapq.heappush(queue, (distance_arr[next_node], next_node))
print(distance_arr[b])
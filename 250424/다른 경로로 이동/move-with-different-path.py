# A의 최단 거리 : 다익스트라 알고리즘 사용
# A의 최단 경로 기억 : union find 알고리즘 사용
# A가 거쳐간 경로 파악 : union find 배열을 통해 파악
import heapq
import sys
INF = sys.maxsize
def get_min_distance_path_set(previous_number_arr, start, end):
    min_distance_path_set = set()
    previous_number = previous_number_arr[end]
    min_distance_path_set.add((previous_number, end))
    min_distance_path_set.add((end, previous_number))

    while previous_number != start:
        min_distance_path_set.add((previous_number, previous_number_arr[previous_number]))
        min_distance_path_set.add((previous_number_arr[previous_number], previous_number))
        previous_number = previous_number_arr[previous_number]
    return min_distance_path_set
def djikstra(start, end, graph, min_distance_path_set, previous_number_arr):
    distance_arr = [INF for _ in range(n+1)]
    # start 방문
    distance_arr[start] = 0
    queue = [(0, start)]

    # 큐가 빌 때까지
    while queue:
        current_distance, current_number = heapq.heappop(queue)
        # 만약 거리가 같지 않으면 스킵
        if distance_arr[current_number] != current_distance:
            continue
        
        # 연결된 모든 정점에 대한 최단 거리
        for next_distance, next_number in graph[current_number]:
            # 만약 이미 방문한 곳이라면 스킵
            if (next_number, current_number) in min_distance_path_set:
                continue
            total_distance = current_distance+next_distance
            if total_distance <= distance_arr[next_number]:
                # 갱신
                distance_arr[next_number] = total_distance
                
                # 큐에 추가
                heapq.heappush(queue, (total_distance, next_number))

                # previous_number_arr 갱신
                previous_number_arr[next_number] = current_number
    return distance_arr
        
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, length = map(int, input().split())
    graph[a].append((length, b))
    graph[b].append((length, a))

# 이미 방문한 경로
# 처음엔 없다.
previous_number_arr = [-1 for _ in range(n+1)] 
djikstra(1, n, graph, set(), previous_number_arr)

min_distance_path_set = get_min_distance_path_set(previous_number_arr, 1, n)
previous_number_arr = [-1 for _ in range(n+1)] 

min_distance_arr = djikstra(1, n, graph, min_distance_path_set, previous_number_arr)
min_distance_path_set = get_min_distance_path_set(previous_number_arr, 1, n)

print(min_distance_arr[n])

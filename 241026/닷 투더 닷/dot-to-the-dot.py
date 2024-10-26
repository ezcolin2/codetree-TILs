import sys
import heapq
import math
INF = sys.maxsize

# start에서 end까지 가는데 최소 시간 구하기
def djikstra(graph, start, end, x):
    # 노드 개수
    n = len(graph)-1

    # 최단 거리 리스트
    distance = [INF]*(n+1)
    
    # start에서 해당 노드까지의 C값 중 최소 값
    min_value = [INF]*(n+1)

    # start에서 해당 노드까지의 모든 선분들의 L값 합
    sum_value = [0]*(n+1)

    # 시작점 넣기
    distance[start] = 0
    queue = [(distance[start], start, 0, INF)]

    # 탐색 시작
    while queue:
        # 최단 거리가 확정된 노드를 가져온다.
        curr_distance, curr_node, curr_sum_l, curr_min_c = heapq.heappop(queue)

        # 최신 정보와 맞지 않으면 스킵
        if distance[curr_node] != curr_distance:
            continue

        # 연결된 모든 점에 대해서 최단 거리 갱신
        for next_node, next_l, next_c in graph[curr_node]:

            # next_node에 대해서 A, B, distance 값 구하기
            next_sum_l = curr_sum_l + next_l
            next_min_c = min(curr_min_c, next_c)
            next_distance = next_sum_l + x/next_min_c
            # 시간이 더 적게 걸린다면 갱신
            if distance[next_node] >= next_distance:
                distance[next_node] = next_distance
                
                # 큐에도 넣기
                heapq.heappush(queue, (distance[next_node], next_node, next_sum_l, next_min_c))
    return distance[end]

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    i, j, l, c = map(int, input().split())
    graph[i].append((j, l, c))
    graph[j].append((i, l, c))
print(math.floor(djikstra(graph, 1, n, x)))
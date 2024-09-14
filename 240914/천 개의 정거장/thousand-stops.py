import sys
import heapq
input = sys.stdin.readline
# 최대 값
INF = sys.maxsize
# 인접 리스트 그래프
graph = [[] for _ in range(1001)]

# 해당 점까지 도달하는데 드는 최단 비용
dist = [(INF, INF)]*1001

a, b, n = map(int, input().split())
for _ in range(n):
    cost, cnt = map(int, input().split())
    arr = list(map(int, input().split()))
    # 해당 경로 중 두 개를 골라서 간선으로 만든다.
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            graph[arr[i]].append((cost, j-i, arr[j]))

# 큐 생성
queue = []
dist[a] = (0, 0)
heapq.heappush(queue, (0, 0, a))

while queue:
    # 최소 값을 가진 점 가져오기
    temp_cost, temp_time, temp_number = heapq.heappop(queue)
    
    # 만약 다르면 패스 
    if dist[temp_number][0] != temp_cost or dist[temp_number][1] != temp_time:
        continue

    # 연결된 모든 점의 최소 값 갱신
    for next_cost, next_time, next_cnt in graph[temp_number]:
        # 만약 저장된 최소 비용보다 작다면
        if dist[next_cnt] >= (temp_cost + next_cost, temp_time + next_time):
            # 최소 비용 갱신
            dist[next_cnt] = (temp_cost + next_cost, temp_time + next_time)
            heapq.heappush(queue, (dist[next_cnt][0], dist[next_cnt][1], next_cnt))

if dist[b][0] == INF:
    print(-1, -1)
else:
    print(dist[b][0], dist[b][1])
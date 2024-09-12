import sys
import heapq
input = sys.stdin.readline
# 최대 값
INF = sys.maxsize

# 인접 리스트 그래프
graph = [[] for _ in range(1001)]

# 해당 점까지 도달하는데 드는 최단 비용
min_cost = [INF]*1001

# 해당 점까지 도달하는데 드는 최단 비용이 여러 개라면 그 중 최단 시간
min_time = [INF]*1001

a, b, n = map(int, input().split())
for _ in range(n):
    cost, cnt = map(int, input().split())
    arr = list(map(int, input().split()))
    # 해당 경로 중 두 개를 골라서 간선으로 만든다.
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            graph[arr[i]].append((cost, arr[j], j-i))

# 큐 생성
queue = []
min_cost[a] = 0
min_time[a] = 0
heapq.heappush(queue, (0, a, 0))

while queue:
    # 최소 값을 가진 점 가져오기
    temp_cost, temp_number, temp_time = heapq.heappop(queue)
    
    # 만약 다르면 패스 
    if min_cost[temp_number] != temp_cost or min_time[temp_number] != temp_time:
        continue

    # 연결된 모든 점의 최소 값 갱신
    for next_cost, next_cnt, next_time in graph[temp_number]:
        # 만약 저장된 최소 비용보다 작다면
        if min_cost[next_cnt] > temp_cost + next_cost:
            # 최소 비용 갱신
            min_cost[next_cnt] = temp_cost + next_cost
            # 최소 시간 갱신
            min_time[next_cnt] = temp_time + next_time
            # 우선순위 큐에 넣기
            heapq.heappush(queue, (min_cost[next_cnt], next_cnt, min_time[next_cnt]))
        # 만약 저장된 최소 비용과 같다면
        elif min_cost[next_cnt] == temp_cost + next_cost:
            # 최소 시간 갱신
            min_time[next_cnt] = min(min_time[next_cnt], temp_time + next_time)
if min_cost[b] == INF:
    print(-1, -1)
else:
    print(min_cost[b], min_time[b])
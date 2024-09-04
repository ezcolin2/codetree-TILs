import heapq
import sys
n, m = map(int, input().split())
a, b = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, val = map(int, input().split())
    graph[x].append((y, val))
    graph[y].append((x, val))

def djikstra(min_val):
    visited = [False]*(n+1)
    queue = [a]
    visited[a] = True
    res = sys.maxsize
    while queue:
        x = heapq.heappop(queue)
        for next_x, val in graph[x] :
            # 방문하지 않았고 만족도가 min_val보다 높을 때만
            if not visited[next_x] and val >= min_val:
                visited[next_x] = True
                heapq.heappush(queue, next_x)
                res = min(res, val)
    if visited[b]:
        return res
    else:
        return -1

left, right = 0, 1000000000
real_res = 0
while left<=right:
    mid = (left+right)//2
    res = djikstra(mid)
    if res == -1:
        right = mid-1
    else:
        left = mid+1
        real_res = max(real_res, mid)
print(real_res)
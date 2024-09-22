import sys
from collections import deque
INF = sys.maxsize
n = int(input())

# n을 1로 만들기 위해 최소
def bfs(n):
    visited = [False]*(n+1)
    visited[n] = True
    queue = deque([(n, 0)])
    while queue:
        number, cnt = queue.popleft()
        if number == 1:
            return cnt
        # 빼기
        if number -1 > 0 and not visited[number-1]:
            queue.append((number-1, cnt+1))
        # 더하기
        if number + 1 <= n and not visited[number+1]:
            queue.append((number+1, cnt+1))
        # 2로 나누기
        if number%2 == 0 and not visited[number//2]:
            queue.append((number//2, cnt+1))
        # 3으로 나누기
        if number%3 == 0 and not visited[number//3]:
            queue.append((number//3, cnt+1))
print(bfs(n))
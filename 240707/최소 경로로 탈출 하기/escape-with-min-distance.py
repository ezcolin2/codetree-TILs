import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 방문 여부
visited = [[False for _ in range(m)] for _ in range(n)]

# 갈 수 있는지
def can_go(x, y):
    return 0<=x<n and 0<=y<m and not visited[x][y] and arr[x][y] == 1

# 너비 우선 탐색으로 최단 거리를 구한다.
def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0] = True

    # 큐가 빌 때까지
    while(queue):
        # 큐에서 꺼낸다.
        x, y, distance = queue.popleft()

        # 동서남북으로 탐색을 하면서 탐색이 가능하면 큐에 넣는다.
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if can_go(nx, ny):
                # 도착했다면
                if nx == n-1 and ny == m-1:
                    print(distance+1)
                    exit()
                queue.append((nx, ny, distance+1))
                visited[nx][ny] = True
    print(-1)

bfs()
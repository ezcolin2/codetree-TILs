from collections import deque
import sys
input = sys.stdin.readline

# n : 격자의 크기 n x n
# h : 사람의 수
# m : 비를 피할 수 있는 공간의 수
n, h, m = map(int, input().split())

# 0 : 이동할 수 있는 공간
# 1 : 이동할 수 없는 공간
# 2 : 사람이 서 있는 곳
# 3 : 비를 피할 수 있는 곳
arr = [list(map(int, input().split())) for _ in range(n)]

# 각 쉘터에서 도달 가능한 거리
distances = [[0 for _ in range(n)] for _ in range(n)]

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 방문 여부
visited = [[False for _ in range(n)] for _ in range(n)]

# 갈 수 있는지
def can_go(x, y):
    return 0<=x<n and 0<=y<n and not visited[x][y] and arr[x][y] != 1

# 너비 우선 탐색
# 쉘터에서 사람이 있는 곳으로 거꾸로 탐색을 한다.
def bfs():
    queue = deque()
    # 모든 쉘터의 위치를 넣는다.
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 3:
                queue.append((i, j))
                visited[i][j] = True
    
    # 큐가 빌 때까지 반복한다
    while queue:
        x, y = queue.popleft()

        # 동서남북 탐색 
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 갈 수 있다면
            if can_go(nx, ny):
                visited[nx][ny] = True
                distances[nx][ny] = distances[x][y] + 1
                queue.append((nx, ny))

bfs()
for i in range(n):
    for j in range(n):
        # 사람이 있는 공간이고 도착했다면 그대로 둠
        if arr[i][j] == 2 and distances[i][j] > 0:
            continue

        # 사람이 있는 공간인데 도착하지 못했으면 -1로 변경
        elif arr[i][j] == 2 and distances[i][j] == 0:
            distances[i][j] = -1
        
        # 모두 아니라면 0 저장
        else:
            distances[i][j] = 0

for i in range(n):
    for j in range(n):
        print(distances[i][j], end = ' ')
    print()
import sys
input = sys.stdin.readline
n, r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
r, c = r-1, c-1

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = [(r, c)]
visited = [arr[r][c]]
while queue:
    x, y = queue.pop()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<n and 0<=ny<n and arr[nx][ny] > arr[x][y]:
            queue.append((nx, ny))
            visited.append(arr[nx][ny])
            break


for i in visited:
    print(i, end= ' ')
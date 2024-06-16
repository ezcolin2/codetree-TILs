import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
starts = [list(map(int, input().split())) for _ in range(k)]

# 큐
queue = []

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 갈 수 있는지
def canGo(x, y):
    return 0<=x<n and 0<=y<n and arr[x][y] == 0
# bfs
# 갈 수 있는 경우에만 시작 (시작점은 갈 수 있는 곳만 주어짐)
def bfs(x, y):
    cnt = 0
    if (arr[x][y] == 0):
        cnt += 1
        # 방문
        arr[x][y] = 1
        # 시작점 큐에 넣음
        queue.append([x, y])
    # 큐가 빌 때까지
    while len(queue) > 0:
        # 꺼냄
        tempX, tempY = queue.pop()
        for i in range(4):
            nx, ny = tempX + dx[i], tempY + dy[i]
            # 갈 수 있다면 큐에 넣고 개수 증가
            if canGo(nx, ny):
                # 방문
                arr[nx][ny] = 1
                queue.append([nx, ny])
                cnt+=1
    return cnt
res = 0
for x, y in starts:
    res += bfs(x-1, y-1)
print(res)
import sys
input = sys.stdin.readline
from collections import deque
# n : 격자의 크기 n x n
# k : 시작 점의 수
# m : 치워야 할 돌의 개수
n, k, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
startDots = [list(map(int, input().split())) for _ in range(k)]
rockDots = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            rockDots.append([i, j])
# dx, dy 정의
# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 방문 여부
def can_go(x, y, visited):
    return 0<=x<n and 0<=y<n and not visited[x][y] and arr[x][y] == 0
# bfs 방식으로 k개의 시작점으로부터 방문이 가능한 서로 다른 칸의 수를 반환하는 함수
def bfs(arr):
    visited = [[False for _ in range(n)] for _ in range(n)]

    visitedCnt = 0 # 지금까지 방문한 횟수
    queue = deque() # 큐
    # 시작 점들을 모두 큐에 넣는다.
    for dot in startDots:
        queue.append([dot[0], dot[1]])
    
    # 큐가 빌 때까지 반복
    while(queue):
        # 큐에서 값을 빼온다.
        x, y = queue.popleft()
        if can_go(x, y, visited):
            visited[x][y] = True # 방문
            visitedCnt += 1 
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            # 갈 수 있다면
            if can_go(nx, ny, visited):
                visited[nx][ny] = True # 방문
                visitedCnt += 1
                queue.append([nx, ny])
    return visitedCnt

max_val = 0
# 돌들 중 m개를 선택하는 함수
def make_combination(idx, cnt):
    global max_val
    if idx >= len(rockDots):
        return
    # m개를 모두 선택했다면
    if cnt == m:
        max_val = max(max_val, bfs(arr))
        return

    x, y = rockDots[idx]

    # x행 y열 뽑기
    arr[x][y] = 0
    make_combination(idx+1, cnt+1)
    arr[x][y] = 1

    # 뽑지 않기
    make_combination(idx+1, cnt)

make_combination(0, 0)

print(max_val)
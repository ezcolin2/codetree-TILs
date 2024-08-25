import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
r, c = map(lambda x : int(x) -1, input().split())
arr = [list(input().rstrip()) for _ in range(n)]

# 오른쪽의 방향
# 정면 방향 : 우하좌상
# 인덱스가 늘어나면 시계 방향
# 인덱스가 줄어들면 반 시계 방향
rx = [1, 0, -1, 0]
ry = [0, -1, 0, 1]

# 정면 방향
# 정면 방향 : 우하좌상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 이동하지 못 하는 경우
# 1. 사방이 모두 벽으로 가로막혀 있을 때
# 2. 이미 방문한 곳을 방문하려고 할 때

x, y = r, c
move_cnt =  0 # 이동 횟수
visited = [[False]*n for _ in range(n)]
direction_idx = 0 # 방향

# 가장 먼저 탈출할 수 있는 곳인지 판단
def can_escape(start_x, start_y):
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and arr[nx][ny] == '.':
                queue.append((nx, ny))
                visited[nx][ny] = True

    # 가장 자리를 방문했다는 뜻은 탈출이 가능하다는 뜻
    for i in range(n):
        if visited[0][i]:
            return True
        if visited[-1][i]:
            return True
        if visited[i][0]:
            return True
        if visited[i][-1]:
            return True
    return False
    
if not can_escape(x, y):
    print(-1)
    exit()
visited = [[False]*n for _ in range(n)]

previous_x, previous_y = x, y
# 미로에서 탈출 할 때까지
while 0<=x<n and 0<=y<n:
    
    # 이미 방문했다는 것은 무한 반복이 일어나고 있다는 뜻
    if visited[x][y] and x == r and y == c and (x != previous_x or y != previous_y):
        print(-1)
        exit()
    previous_x, previous_y = x, y
    visited[x][y] = True
    # 현재 정면 방향으로 이동했을 때 좌표
    nx, ny = x+dx[direction_idx], y+dy[direction_idx]
    if nx<0 or nx>=n or ny<0 or ny>=n:
        move_cnt += 1
        break


    # 만약 정면 방향에 벽이 있다면
    if arr[nx][ny] == '#':
        rotation_cnt = 0
        while arr[nx][ny] == '#':
            # 4번 이상 회전했다는 뜻은 빠져나갈 곳이 없다는 뜻
            if rotation_cnt > 4:
                print(-1)
                exit()
            # 반 시계 방향 회전
            direction_idx = (direction_idx-1)%4
            nx, ny = x+dx[direction_idx], y+dy[direction_idx]
            rotation_cnt += 1
        # x, y = nx, ny
        # move_cnt += 1

    else:
        # 만약 정면 방향으로 이동한 후 오른쪽에 벽이 없다면
        nrx, nry = nx+rx[direction_idx], ny+ry[direction_idx]
        if arr[nrx][nry] == '.':

            # 시계 방향 회전 후 이동
            direction_idx = (direction_idx+1)%4
            x, y = nx, ny
            move_cnt += 1
        # 만약 정면 방향으로 이동한 후 현재 방향의 오른ㄹ쪽에벽이 있다면
        else:
            x, y = nx, ny
            move_cnt += 1
    
print(move_cnt)
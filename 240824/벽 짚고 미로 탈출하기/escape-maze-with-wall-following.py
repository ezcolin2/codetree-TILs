import sys
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
# 미로에서 탈출 할 때까지
while 0<=x<n and 0<=y<n:
    # 이미 방문했다는 것은 무한 반복이 일어나고 있다는 뜻
    if visited[x][y] or arr[x][y] == '#':
        print(-1)
        exit()
    visited[x][y] = True
    # 현재 정면 방향으로 이동했을 때 좌표
    nx, ny = x+dx[direction_idx], y+dy[direction_idx]
    


    # 만약 정면 방향에 벽이 있다면
    if arr[nx][ny] == '#':
        # 반 시계 방향 회전
        direction_idx = (direction_idx-1)%4
        x, y = x+dx[direction_idx], y+dy[direction_idx]
        move_cnt += 1

    else:
        # 만약 정면 방향으로 이동한 후 오른쪽에 벽이 없다면
        nrx, nry = nx+rx[direction_idx], ny+ry[direction_idx]
        if arr[nrx][nry] == '.':

            # 시계 방향 회전 후 이동
            direction_idx = (direction_idx+1)%4
            x, y = nx, ny
            move_cnt += 1
        # 만약 현재 방향의 오른ㄹ쪽에 벽이 있다면
        else:
            x, y = nx, ny
            move_cnt += 1
print(move_cnt)
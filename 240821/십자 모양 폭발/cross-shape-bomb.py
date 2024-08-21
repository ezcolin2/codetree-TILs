import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
r, c = map(lambda x:int(x)-1, input().split())

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def can_go(x, y):
    return 0<=x<n and 0<=y<n

iteration = arr[r][c]
# 기존 배열의 터진 부분을 모두 0으로 만든다.
arr[r][c] = 0
for i in range(4):
    nx, ny = r+dx[i], c+dy[i]
    for _ in range(iteration - 1):
        if can_go(nx, ny):
            arr[nx][ny] = 0
            nx, ny = nx+dx[i], ny+dy[i]

new_arr = [[0]*n for _ in range(n)]
for i in range(n):
    idx = n-1
    for j in range(n-1, -1, -1):
        # 0이 아닐 때만 추가
        if arr[j][i] != 0: 
            new_arr[idx][i] = arr[j][i]
            idx-=1
for row in new_arr:
    for col in row:
        print(col, end=' ')
    print()
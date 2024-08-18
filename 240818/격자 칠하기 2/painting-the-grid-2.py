import sys
input = sys.stdin.readline

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# (x, y)에서 시작했을 때 색칠 가능한 칸의 개수
def bfs(x, y, visited, d):
    visited_cnt = 1
    queue = [(x, y)]
    visited[x][y] = True
    while queue:
        x, y = queue.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and abs(arr[x][y] - arr[nx][ny]) <= d:
                visited_cnt += 1
                queue.append((nx, ny))
                visited[nx][ny] = True
    return visited_cnt
# 임의로 시작칸을 잘 정한 후, 
# 칸에 쓰인 숫자가 현재 칸의 숫자와 D 이하로 차이나는 상, 하, 좌, 우로 인접한 칸으로 이동했을 때
# 색칠된 칸이 전체 칸의 반 이상이 될 수 있는지
def is_possible(d):
    visited = [[False]*n for _ in range(n)]
    # 모든 시작 점
    for i in range(n):
        for j in range(n):
            visited_cnt = bfs(i, j, visited, d)
            if visited_cnt >= round((n**2)//2):
                return True
    return False

def parametric_search():
    res = 1000000
    left, right = 0, 1000000
    while left <= right:
        mid = (left + right)//2
        # 가능하다면 더 작은 범위 체크
        if is_possible(mid):
            right = mid - 1
            res = min(res, mid)
        else:
            left = mid + 1
    return res

res = parametric_search()
print(res)
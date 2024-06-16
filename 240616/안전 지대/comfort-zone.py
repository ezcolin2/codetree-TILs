import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 방문하지 않았고 K보다 높이가 큰 경우에만 방문할 수 있음
def canGo(x, y, k, visited):
    return 0<=x<n and 0<=y<m and not visited[x][y] and arr[x][y] > k

# 하나의 안전 영역을 모두 탐색
# 갈 수 있는 경우에만 실행
def dfs(x, y, k, visited):
    visited[x][y] = True
    # 동서남북 갈 수 있는 곳 탐색
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        # 갈 수 있다면 방문
        if canGo(nx, ny, k, visited):
            dfs(nx, ny, k, visited)

# 안전 영역의 개수를 구하는 함수
def getRangeCnt(k):
    # 방문 여부
    visited = [[False for _ in range(m)] for _ in range(n)]
    # 안전 영역의 개수
    cnt = 0
    for i in range(n):
        for j in range(m):
            # 아직 가지 않은 곳이 있다면 dfs 실행
            if canGo(i, j, k, visited):
                dfs(i, j, k, visited)
                # dfs가 끝났다는 것은 안전 영역을 하나 구했다는 뜻
                cnt+=1
    return cnt

# 모든 K에 대해서 구한 뒤 최대 안전 영역의 수 구함
def solution():
    res = 0
    maxK = 1
    for k in range(1, 101):
        temp = getRangeCnt(k)
        # 안전 영역이 0이라는 뜻은 k가 아무리 올라가도 무조건 0 
        if temp == 0:
            return res, maxK
        if res < temp:
            res = temp
            maxK = k
            
        res = max(res, temp)
    return res, maxK

res, maxK = solution()
print(maxK, res)
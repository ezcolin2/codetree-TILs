import sys
input = sys.stdin.readline
# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# n : 격자의 크기 n x n
# k : 고를 도시의 수 
# u : 최저 높이 차
# d : 최고 높이 차
n, k, u, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 고른 좌표
selected_locations = []

# 갈 수 있는 서로 다른 도시의 수 
def get_different_cities(selected_locations):
    # 방문 여부
    visited = [[False]*n for _ in range(n)]

    # 선택된 도시들을 모두 큐에 넣음 
    queue = [location for location in selected_locations]
    while queue:
        x, y = queue.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 방문 가능하다면
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and u<=abs(arr[nx][ny] - arr[x][y])<=d:
                visited[nx][ny] = True
                
                queue.append((nx, ny))
    return sum([row.count(True) for row in visited])


max_res = k
# 현재까지 selected_cnt개를 뽑은 상태에서 [idx//n][idx%n] 좌표를 뽑을 것인지
def choose(idx, selected_cnt):
    global max_res
    # 다 순회했다면 
    if idx == n**2:
        # 다 뽑았다면 
        if selected_cnt == k:
            visited_cnt = get_different_cities(selected_locations)
            max_res = max(max_res, visited_cnt)
        return
    # 뽑음
    selected_locations.append((idx // n, idx % n))
    choose(idx+1, selected_cnt + 1)
    selected_locations.pop()

    # 안 뽑음
    choose(idx+1, selected_cnt)
choose(0, 0)
print(max_res)
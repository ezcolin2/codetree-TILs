# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 최대 높이, 최소 높이  차이가 difference 이하로 이동하는게 가능한지
def is_possible(arr, difference):
    n = len(arr)
    m = len(arr[0])
    max_val = arr[0][0]
    min_val = arr[0][0]
    visited = [[False]*m for _ in range(n)]
    # 첫 번째 방문
    visited[0][0] = True
    stack = [(0, 0)]
    
    # dfs 진행
    while stack:
        # 스택에서 꺼낸다.
        x, y = stack.pop()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            # 범위에서 벗어나거나 방문했다면 스킵
            if nx<0 or nx>=n or ny<0 or ny>=m or visited[nx][ny]:
                continue
            
            # 차이가 넘어가면 스킵
            if max(max_val, arr[nx][ny])-min(min_val, arr[nx][ny]) > difference:
                continue
            
            # 갱신
            max_val = max(max_val, arr[nx][ny])
            min_val = min(min_val, arr[nx][ny])

            # 끝에 도달했다면 가능한 것
            if nx == n-1 and ny == m-1:
                return True

            # 방문
            stack.append((nx, ny))
            visited[nx][ny] = True
    return False

# 가장 짧은 거리 차 구하기 
def get_min_difference(arr):
    min_difference = 500
    left, right = 0, 500
    # 이진 탐색 시작
    while left<=right:
        mid = (left+right)//2
        if is_possible(arr, mid):
            min_difference = min(min_difference, mid)
            right = mid-1
            continue
        left = mid+1
    return min_difference


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
print(get_min_difference(arr))
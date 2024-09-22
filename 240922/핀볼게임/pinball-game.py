n = int(input())
arr = [[0]*(n+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(n)] + [[0]*(n+2)]
# 동서남북 
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 바를 만났을 때 바뀌는 진행 방향 
# bar_type=1 : / 
# bar_type=2 : \
def change_direction(direction_idx, bar_type):
    # 동 -> 북
    if direction_idx == 0 and bar_type ==1:
        return 3
    # 서 -> 남
    if direction_idx == 1 and bar_type == 1:
        return 2
    # 남 -> 서
    if direction_idx == 2 and bar_type ==1:
        return 1
    # 북 -> 동
    if direction_idx == 3 and bar_type == 1:
        return 0

    # 동 -> 남
    if direction_idx == 0 and bar_type == 2:
        return 2
    # 서 -> 북
    if direction_idx == 1 and bar_type == 2:
        return 3
    # 남 -> 동
    if direction_idx == 2 and bar_type == 2:
        return 0
    # 북 -> 서
    if direction_idx == 3 and bar_type == 2:
        return 1

# 핀볼 게임을 진행하는데 걸리는 시간 반환
def get_pinball_time(arr, start_x, start_y, start_direction_idx):
    n = len(arr)-2
    x, y, direction_idx = start_x, start_y, start_direction_idx
    # 나가는 시간
    time = 1
    # 벗어날 때까지 반복
    while True:
        nx, ny = x + dx[direction_idx], y + dy[direction_idx]
        # 벗어나면 시간 반환
        if nx < 1 or nx > n or ny < 1 or ny > n:
            return time
        # 바를 만났다면 방향 전환
        if arr[nx][ny] != 0:
            direction_idx = change_direction(direction_idx, arr[nx][ny])
        # 현재 위치 갱신
        x, y = nx, ny
        time += 1

# 최대 시간 반환
def get_max_time(arr):
    max_time = 0
    n = len(arr)-2
    # 동
    for i in range(1, n+1):
        temp_time = get_pinball_time(arr, i, 0, 0)
        max_time = max(max_time, temp_time)
    # 서
    for i in range(1, n+1):
        temp_time = get_pinball_time(arr, i, n+1, 1)
        max_time = max(max_time, temp_time)
    # 남
    for i in range(1, n+1):
        temp_time = get_pinball_time(arr, 0, i, 2)
        max_time = max(max_time, temp_time)
    # 북
    for i in range(1, n+1):
        temp_time = get_pinball_time(arr, n+1, i, 3)
        max_time = max(max_time, temp_time)
    return max_time
print(get_max_time(arr))
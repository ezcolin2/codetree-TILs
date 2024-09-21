from collections import deque
from copy import deepcopy
n, m, t, k = map(int, input().split())
arr = [[deque([]) for _ in range(n+1)] for _ in range(n+1)]
# R L U D
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for i in range(1, m+1):
    r, c, d, v = input().split()
    r, c, v = map(int, [r, c, v])
    arr[r][c].append((d, v, i))

get_opposite_direction = {
    'R': 'L',
    'L': 'R',
    'U': 'D',
    'D': 'U'
}
get_dx = {
    'R': 0,
    'L': 0,
    'U': -1,
    'D': 1
}
get_dy = {
    'R': 1,
    'L': -1,
    'U': 0,
    'D': 0
}

# 초과한 만큼 반대 방향
def move_opposite_position(n, x):
    # 양의 방향으로 초과했다면
    if x > n:
        return n-(x-n)
    # 음의 방향으로 초과했다면
    if x < 1:
        return -x+2
    return x

def get_next_direction(n, x, y, speed, direction):
    # 이동할 횟수 줄이기
    speed %= 2*(n-1)
    # 다음 위치 구하기
    dx, dy = get_dx[direction], get_dy[direction]
    nx, ny = x + dx*speed, y + dy*speed
    # 만약 U 또는 D라면
    if dx != 0:
        x = x + dx*speed
        # 양의 방향으로 초과했다면
        if x > n:
            return get_opposite_direction[direction]
        # 음의 방향으로 초과했다면
        if x < 1:
            return get_opposite_direction[direction]
        return direction
    else:
        y = y + dy*speed
        # 양의 방향으로 초과했다면
        if y > n:
            return get_opposite_direction[direction]
        # 음의 방향으로 초과했다면
        if y < 1:
            return get_opposite_direction[direction]
        return direction
# 다음 위치 
def get_next_location(n, x, y, speed, direction):
    # 이동할 횟수 줄이기
    speed %= 2*(n-1)
    # 다음 위치 구하기
    dx, dy = get_dx[direction], get_dy[direction]
    nx, ny = x + dx*speed, y + dy*speed

    # 초과했다면 반대 방향으로 
    nx, ny = move_opposite_position(n, nx), move_opposite_position(n, ny)
    return nx, ny

# 일 초 동안 움직임
def move_one_second(arr):
    new_arr = deepcopy(arr)
    n = len(arr)-1
    for i in range(1, n+1):
        for j in range(1, n+1):
            # 해당 위치에 존재하는 모든 구슬을 이동한다.
            # 현재 위치에 존재하는 구슬 횟수
            cnt = len(arr[i][j])
            for _ in range(cnt):
                d, v, number = new_arr[i][j].popleft()
                nx, ny = get_next_location(n, i, j, v, d)
                nd = get_next_direction(n, i, j, v, d)
                new_arr[nx][ny].append((nd, v, number))
    return new_arr

def remove_duplicate_marbles(arr, k):
    new_arr = deepcopy(arr)
    n = len(arr)-1
    for i in range(1, n+1):
        for j in range(1, n+1):
            # 최대 개수를 넘었다면
            if len(arr[i][j]) > k:
                queue = list(new_arr[i][j])

                queue.sort(key = lambda x:(-x[1], -x[2]))
                new_arr[i][j] = deque(queue[:k])
    return new_arr

# 남아있는 구슬 개수
def get_remain_marble_count(arr):
    res = 0
    for row in arr:
        for queue in row:
            res += len(queue)
    return res
arr = move_one_second(arr)
arr = remove_duplicate_marbles(arr, k)
print(get_remain_marble_count(arr))
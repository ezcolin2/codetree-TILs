n, m, k = map(int, input().split())
# 사과 위치
apples = [[0]*(n+1) for _ in range(n+1)]
# 다음 몸통의 방향
snake_directions = [[0]*(n+1) for _ in range(n+1)]
# 사과 위치 저장
for _ in range(m):
    x, y = map(int, input().split())
    apples[x][y] = 1
directions = [tuple(input().split()) for _ in range(k)]

# 현재 뱀 머리 위치
current_head = (1, 1)
# 현재 뱀 꼬리 위치 
current_tail = (1, 1)
# 스네이크 조각들 위치
# snake_directions[1][1] = 1
# 꼬리의 이전 방향은 없음

# 동서남북
dx = 0, 0, 1, -1
dy = 1, -1, 0, 0
direction_map = {
    'R': 0,
    'L': 1,
    'D': 2,
    'U': 3
}
opposite_direction_map = {
    'R': 'L',
    'L': 'R',
    'D': 'U',
    'U': 'D'
}
# 뱀을 direction 방향으로 한 번 움직인다. 
# 머리만 움직인다.
# 무조건 움직일 수 있을 때만 움직인다.
def move_head(snake_directions, direction, next_head_location):
    new_snake_directions = [snake_direction[:] for snake_direction in snake_directions]
    head_nx, head_ny = next_head_location
    # 이전 머리에 방향을 부여한다.
    opposite_direction = opposite_direction_map[direction]
    direction_idx = direction_map[opposite_direction]
    head_x, head_y = head_nx+dx[direction_idx], head_ny+dy[direction_idx]
    new_snake_directions[head_x][head_y] = direction
    return new_snake_directions

# 꼬리를 자른다.
def slice_tail(snake_directions, current_tail_location):
    new_snake_directions = [snake_direction[:] for snake_direction in snake_directions]
    tail_x, tail_y = current_tail_location
    # 부여했던 방향을 제거한다.
    new_snake_directions[tail_x][tail_y] = 0
    return new_snake_directions

# 꼬리의 다음 위치를 구한다.
def get_next_tail_location(current_tail_location, direction):
    direction_idx = direction_map[direction]
    tail_x, tail_y = current_tail_location
    tail_nx, tail_ny = tail_x + dx[direction_idx], tail_y + dy[direction_idx]
    return (tail_nx, tail_ny)

# 머리의 다음 위치를 구한다.
def get_next_head_location(current_head_location, direction):
    direction_idx = direction_map[direction]
    head_x, head_y = current_head_location
    head_nx, head_ny = head_x + dx[direction_idx], head_y + dy[direction_idx]
    return (head_nx, head_ny)

# 이동할 수 있는지
def is_valid_location(snake_directions, next_head_location):
    nx, ny = next_head_location
    # 범위를 벗어나지 않고 겹치지 않아야 함
    return 1<=nx<=n and 1<=ny<=n and snake_directions[nx][ny] == 0

# 흐른 시간
time = 0
for direction, count in directions:
    count = int(count)
    for _ in range(count):
        # 시간이 흐른다.
        time += 1
        # 가장 먼저 다음 머리의 위치를 구한다.
        next_head_location = get_next_head_location(current_head, direction)
        # 만약 다음 머리로 이동이 불가능하다면 끝난다.
        if not is_valid_location(snake_directions, next_head_location):
            print(time)
            exit()
        head_nx, head_ny = next_head_location
        # 일단 머리만 이동시킨다.
        snake_directions = move_head(snake_directions, direction, next_head_location)
        current_head = next_head_location
        # 사과가 있다면 끝낸다.
        if apples[head_nx][head_ny]:
            continue
        # 사과가 없다면 꼬리를 자른다.
        next_tail_location = get_next_tail_location(current_tail, snake_directions[current_tail[0]][current_tail[1]])
        snake_directions = slice_tail(snake_directions, current_tail)
        current_tail = next_tail_location
print(time)
import sys
input = sys.stdin.readline
dice = [1, 2, 3, 4, 5, 6] # 윗면, 앞면, 오른쪽 면, 왼쪽 면, 뒷 면, 아랫 면
# next_number[current_number][idx] : 현재 바닥면이 current_number일 때 idx 방향으로 굴렸을 때 다음 바닥면의 값
def next_dice(dice, direction_idx):
    if direction_idx == 0: # 왼
        new_dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif direction_idx == 1: # 오
        new_dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif direction_idx == 2: # 위
        new_dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
    else:
        new_dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    return new_dice


# 방향 -> 인덱스
direction_idx_map = {
    'L': 0,
    'R': 1,
    'U': 2,
    'D': 3
}

# LRUD 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m, r, c = map(int, input().split())
directions = list(input().split())



# 주사위 굴리기 시작
def roll_dice(directions, n, r, c):
    # 격자판
    arr = [[0]*(n+1) for _ in range(n+1)]
    arr[r][c] = 6
    x, y = r, c
    current_dice = [1, 2, 3, 4, 5, 6]
    for direction in directions:
        # 반복문 첫 시작의 상태는 이미 전개도에 숫자가 찍힌 상태
        direction_idx = direction_idx_map[direction]
        # 다음 격자판 위치
        nx, ny = x+dx[direction_idx], y+dy[direction_idx]
        # 범위를 벗어나면 패스
        if nx < 1 or nx > n or ny < 1 or ny > n:
            continue
        # 주사위를 direction_idx 방향으로 굴렸을 때 주사위 전개도 모양
        current_dice = next_dice(current_dice, direction_idx)
        # 격자에 아랫면 숫자 찍음
        arr[nx][ny] = current_dice[5]
        x, y = nx, ny
    return arr
res_arr = roll_dice(directions, n, r, c)
res = sum([sum(row) for row in res_arr])
print(res)
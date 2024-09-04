import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(lambda x:[int(x)], input().split())) for _ in range(n)]
numbers = list(map(int, input().split()))

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
# 번호마다 좌표와 idx를 저장한다.
# locations[2] = 0, 1, 2의 의미는 (0, 1) 좌표에 존재하는 리스트의 인덱스 2번에 2가 존재한다는 뜻
locations = {}

for i in range(n):
    for j in range(n):
        locations[arr[i][j][0]] = (i, j, 0)

# 이동 시작
for number in numbers:
    x, y, idx = locations[number]
    max_val = -1
    # 8방향으로 모두 찾아본다.
    for i in range(8):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            # 해당 위치에 존재하는 모든 숫자를 확인한다.
            for num in arr[nx][ny]:
                if num > max_val:
                    max_val = num

    # 아무 숫자도 없다면 이동하지 않는다.
    if max_val == -1:
        continue
    # 가장 큰 숫자의 위치에 현재 위치의 자신 포함 위에 쌓인 숫자들을 넣는다.
    new_x, new_y, new_idx = locations[max_val]
    arr[new_x][new_y] += arr[x][y][idx:]
    arr[x][y] = arr[x][y][:idx]

    # locations 딕셔너리의 값을 변경한다.
    for i, num in enumerate(arr[new_x][new_y]):
        locations[num] = (new_x, new_y, i)

for i in range(n):
    for j in range(n):
        if len(arr[i][j]) == 0:
            print("None")
        else:
            while arr[i][j]:
                print(arr[i][j].pop(), end = ' ')
            print()
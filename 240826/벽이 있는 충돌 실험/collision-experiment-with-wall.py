import sys
input = sys.stdin.readline
# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 문자 -> 인덱스
char_to_idx = {
    'U': 0,
    'R': 1,
    'D': 2,
    'L': 3
}
t = int(input())
for _ in range(t):
    n, m  = map(int, input().split())
    # 방향 저장 2차원 배열
    direction_arr = [[-1]*(n+1) for _ in range(n+1)]
    # 구슬 개수 2차원 배열
    count_arr = [[0]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        x, y, d = input().split()

        # 입력 값 변환
        x, y = int(x), int(y)
        d = char_to_idx[d]

        # 배열 저장
        direction_arr[x][y] = d
        count_arr[x][y] += 1

    # 2n번만큼 반복하면 위치 똑같음
    for _ in range(2*n):
        # 방향 저장 2차원 배열
        new_direction_arr = [[-1]*(n+1) for _ in range(n+1)]
        # 구슬 개수 2차원 배열
        new_count_arr = [[0]*(n+1) for _ in range(n+1)]

        # 2차원 배열 순회하면서 구슬 위치 변경
        for i in range(1, n+1):
            for j in range(1, n+1):
                # 구슬이 있다면
                if count_arr[i][j] > 0:
                    ni, nj = i+dx[direction_arr[i][j]], j+dy[direction_arr[i][j]]
                    # 이동 가능하다면
                    if 1<=ni<=n and 1<=nj<=n:
                        new_direction_arr[ni][nj] = direction_arr[i][j]
                        new_count_arr[ni][nj] += 1
                    # 이동 불가능하다면
                    else:
                        new_direction_arr[i][j] = (direction_arr[i][j] + 2)%4
                        new_count_arr[i][j] += 1
        # for row in count_arr:
        #     for col in row:
        #         print(col, end=' ')
        #     print()
        # print()
        # for row in direction_arr:
        #     for col in row:
        #         print(col, end=' ')
        #     print()
        # print()
        # 중복된 구슬 제거
        for i in range(1, n+1):
            for j in range(1, n+1):
                if new_count_arr[i][j] > 1:
                    new_count_arr[i][j] = 0
                    new_direction_arr[i][j] = -1
        count_arr = new_count_arr
        direction_arr = new_direction_arr

    res = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if count_arr[i][j] == 1:
                res+=1
    # print(count_arr)
    print(res)
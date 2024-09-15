arr = [list(map(int, input().split())) for _ in range(4)]
direction = input()

def after_gravity(arr, direction):
    # 새로운 배열 생성
    new_arr = [[0]*4 for _ in range(4)]
    if direction == 'R':
        for row in range(0, 4):
            # 현재 인덱스
            current_idx = 3
            for col in range(3, -1, -1):
                if arr[row][col] == 0:
                    continue
                new_arr[row][current_idx] = arr[row][col]
                current_idx -= 1
    elif direction == 'L':
        for row in range(0, 4):
            # 현재 인덱스
            current_idx = 0
            for col in range(0, 4):
                if arr[row][col] == 0:
                    continue
                new_arr[row][current_idx] = arr[row][col]
                current_idx += 1        
    elif direction == 'U':
        for col in range(0, 4):
            # 현재 인덱스
            current_idx = 0
            for row in range(0, 4):
                if arr[row][col] == 0:
                    continue
                new_arr[current_idx][col] = arr[row][col]
                current_idx += 1      
    elif direction == 'D':
        for col in range(0, 4):
            # 현재 인덱스
            current_idx = 3
            for row in range(3, -1, -1):
                if arr[row][col] == 0:
                    continue
                new_arr[current_idx][col] = arr[row][col]
                current_idx -= 1      
    return new_arr

def add_same_number(arr, direction):
    # 새로운 배열 생성
    new_arr = [row[:] for row in arr]
    if direction == 'R':
        for row in range(0, 4):
            for col in range(2, -1, -1):
                if new_arr[row][col] == new_arr[row][col+1]:
                    new_arr[row][col] = 0
                    new_arr[row][col+1]*=2
    elif direction == 'L':
        for row in range(0, 4):
            for col in range(1, 4):
                if new_arr[row][col] == new_arr[row][col-1]:
                    new_arr[row][col] = 0
                    new_arr[row][col-1]*=2
    elif direction == 'U':
        for col in range(0, 4):
            for row in range(0, 4):
                if new_arr[row][col] == new_arr[row-1][col]:
                    new_arr[row][col] = 0
                    new_arr[row-1][col]*=2
    elif direction == 'D':
        for col in range(0, 4):
            for row in range(2, -1, -1):
                if new_arr[row][col] == new_arr[row+1][col]:
                    new_arr[row][col] = 0
                    new_arr[row+1][col]*=2
    return new_arr

new_arr = after_gravity(arr, direction)
new_arr = add_same_number(new_arr, direction)
new_arr = after_gravity(new_arr, direction)
for row in new_arr:
    for val in row:
        print(val, end=' ')
    print()
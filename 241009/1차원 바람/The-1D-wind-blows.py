n, m, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
winds = [list(input().split()) for _ in range(q)]

# 왼쪽으로 바람이 불때
def blow_left(arr, row_idx):
    temp = arr[row_idx][0]
    for i in range(len(arr[0])-1):
        arr[row_idx][i] = arr[row_idx][i+1]
    arr[row_idx][-1] = temp

# 오른쪽으로 바람이 불때
def blow_right(arr, row_idx):
    temp = arr[row_idx][-1]
    for i in range(len(arr[0])-1, 0, -1):
        arr[row_idx][i] = arr[row_idx][i-1]
    arr[row_idx][0] = temp

# base_idx 행에서 row_idx 행으로 전파 가능한지
def can_transfer(arr, base_idx, row_idx):
    m = len(arr[0])
    for i in range(m):
        if arr[base_idx][i] == arr[row_idx][i]:
            return True
    return False
blow_left(arr, 1)

blow_right(arr, 2)

for row_idx, direction in winds:
    row_idx = int(row_idx)
    # 이동
    if direction == 'L':
        blow_left(arr, row_idx)
    # 전파 여부 체크
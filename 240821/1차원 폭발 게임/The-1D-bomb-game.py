import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

def bomb(arr):
    if len(arr) == 0:
        return []
    # 연속된 숫자
    number = arr[0]
    # 연속된 횟ㅅ
    cnt = 1

    for i in range(1, len(arr)):
        # 연속되었다면
        if arr[i] == number:
            cnt += 1
        # 연속된 숫자가 아니라면
        else:
            number = arr[i]
            cnt = 1
    
        if cnt >= m:
            # 연속된 숫자 0으로 만듦
            for j in range(i, i-cnt, -1):
                arr[j] = 0
            # 앞으로도 가면서 제거
            for j in range(i+1, len(arr)):
                if arr[j] == number:
                    arr[j] = 0
                else:
                    break
    new_arr = []
    for i in arr:
        if i != 0:
            new_arr.append(i)
    return new_arr

while True:
    new_arr = bomb(arr)
    if len(arr) == len(new_arr):
        break
    arr = new_arr

print(len(new_arr))
for i in new_arr:
    print(i)
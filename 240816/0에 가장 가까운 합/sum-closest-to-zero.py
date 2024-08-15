import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

# two pointer
left = 0
right = len(arr) - 1


# 서로 다른 두 정수의 합
res = abs(arr[right] + arr[left])

# 양 쪽엥서 시작해서 범위를 좁혀오기
while left < right:
    sum_val = arr[right] + arr[left]
    res = min(res, abs(sum_val))
    # 0보다 크다면 right를 줄여서 0에 더 가깝게 할 수 있는지 확인
    if sum_val > 0:
        right -= 1

    # 0보다 작다면 left를 늘여서 0에 더 가깝게 할 수 있는지 확인
    elif sum_val < 0:
        left += 1
    
    # 0이라면 끝냄
    else:
        break
print(res)
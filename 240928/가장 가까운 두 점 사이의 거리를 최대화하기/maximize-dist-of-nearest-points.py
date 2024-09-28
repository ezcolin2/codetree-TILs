n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort()

# 최소 거리가 x인 것이 가능한지
def is_possible(arr, x):
    temp_location = arr[0][0]
    # 점들을 순회하면서 최대한 x에 가깝게 다음 점을 잡는다.
    for start, end in arr[1:]:
        # 최소거리 x가 불가능한다면
        if temp_location + x > end:
            return False
        temp_location = max(temp_location + x, start)
    return True

# parametric search
def parametric_search(arr):
    max_distance = 0
    left, right = 0, 100000000
    while left <= right:
        mid = (left+right)//2
        if is_possible(arr, mid):
            left = mid+1
            max_distance = max(max_distance, mid)
            continue
        right = mid-1
    return max_distance

print(parametric_search(arr))
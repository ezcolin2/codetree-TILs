import sys
input = sys.stdin.readline
n = int(input())
locations = list(map(lambda x:int(x)*100000, input().split()))
speeds = list(map(int, input().split()))

# 특정 점에 대해서 x초 동안 이동 가능한 위치의 범위를 반환한다.
def get_location_range(n, location, speed, x):
    return [max(0, location-speed*x), min(100000000000000, location+speed*x)]

# 모두 도착하는 데 걸리는 시간이 x초 이상인 도착점의 겹치는 범위 반환
# 만약 범위[0] > 범위[1]이라면 해당하는 도착점이 없는 것 
def get_overrapped_location_range(n, locations, speeds, x):
    # 초기 범위
    location_range = get_location_range(n, locations[0], speeds[0], x)
    # 각 위치마다 x초 동안 이동 가능한 범위를 구한다.
    for idx in range(1, n):
        temp_location_range = get_location_range(n, locations[idx], speeds[idx], x)
        location_range[0] = max(location_range[0], temp_location_range[0])
        location_range[1] = min(location_range[1], temp_location_range[1])
    return location_range

# 이진 탐색
def parametric_search(n, locations, speeds):
    left, right = 0, 100000000000000
    res_location_range=[]
    min_time = sys.maxsize
    while left<=right:
        mid = (left+right)//2
        location_range = get_overrapped_location_range(n, locations, speeds, mid)
        if location_range[0] <= location_range[1]:
            right = mid-1
            res_location_range = location_range
            min_time = min(min_time, mid)
        # 만약 범위가 잘못되었다면 불가능
        else:
            left = mid+1
    return min_time

print("{:.4f}".format(round(parametric_search(n, locations, speeds)/10)/10000))
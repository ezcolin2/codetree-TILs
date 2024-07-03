import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
arr.sort()

# 가장 가까운 두 점의 거리가 x가 되는 것이 가능한가.
# 1. (이전 선분에서 마지막으로 배치한 점 + x )와 (현재 선분의 시작 점) 중 큰 값을 저장한다. (+1)
# 2. 한 선분에서 가까운 두 점의 거리가 x가 되도록 최대한 배치한다.
# 3. 1번의 선분에서 마지막으로 배치한 점의 위치를 저장한다.
def is_possible(x):
    if x <= 0:
        return False
    last_dot_location = -x # 이전 선분에서 마지막으로 배치한 점의 위치
    dot_cnt = 0 # 지금까지 배치한 점의 개수
    for start, end in arr: 
        start = max(start, last_dot_location + x)

        # 범위를 넘어서면 continue
        if (start > end):
            continue
        
        # 최대한 배치
        temp_cnt = (end-start)//x + 1
        dot_cnt += temp_cnt
        
        # 마지막 값 갱신
        last_dot_location = start + (temp_cnt - 1)*x
    # 모든 점들을 배치했다면 True
    if (dot_cnt >= n):
        return True
    else:
        return False
# 이진 탐색
res = 0
def binary_search():
    global res
    left, right = 0, 10**18
    while (left <= right):
        mid = (left + right)//2
        if (is_possible(mid)): # 가능하면 더 큰 값도 가능한지 확인
            left = mid + 1
            # 갱신
            res = max(res, mid)
        else:
            right = mid -1

binary_search();
print(res)
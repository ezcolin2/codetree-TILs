import sys
input = sys.stdin.readline

n, m = map(int, input().split())
times = [int(input()) for _ in range(m)]

# time만에 가능한지
def is_possible(time):
    cnt = 0
    # 각 통로마다 times 안에 몇 개 넣을 수 있는지 구함
    for i in times:
        cnt += time // i
    
    # 해당 시간 내에 최대로 넣을 수 있는 개수가 m보다 크면 true
    if cnt >= n:
        return True
    return False

min_time = 10**14
# 이진탐색 시작
left, right = 1, 10**14
while left <= right:
    mid = (left + right)//2

    # 가능하다면 더 줄임
    if is_possible(mid):
        # 가능할 때마다 min_time 갱신
        min_time = min(min_time, mid)
        right = mid-1
    
    # 불가능하다면 더 늘림
    else:
        left = mid+1

print(min_time)
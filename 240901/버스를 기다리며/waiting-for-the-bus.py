import sys
input = sys.stdin.readline
n, m, c = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

# 가장 오래 기다려야 하는 사람이 기다리는 시간이 wait_time 이하인지
def is_possible(wait_time):
    group_cnt = 1 # 총 그룹 수
    current_group_cnt = 1 # 현재 그룹 내부 요소 개수
    for i in range(1, n):
        # 만약 그룹이 꽉 찼거나 기다리는 시간이 길다면 새로운 그룹 생성
        if current_group_cnt == c or arr[i]-arr[i-1] > wait_time:
            current_group_cnt = 0
            group_cnt += 1
        # 기다리는 시간보다 작으면 현재 그룹에 넣기
        elif arr[i]-arr[i-1] <= wait_time:
            current_group_cnt += 1
    # 생성된 그룹의 수가 M 이하인지
    return group_cnt <= m

left, right = 0, 1000000000
res = sys.maxsize
while left <= right:
    mid = (left + right)//2
    if is_possible(mid):
        right = mid-1
        res = min(res, mid)
    else:
        left = mid + 1
print(res)
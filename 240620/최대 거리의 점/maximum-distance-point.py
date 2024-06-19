import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dots = [int(input()) for _ in range(n)]
dots.sort()

# 가장 인접한 두 물건의 거리를 만족하는 경우의 수의 존재 여부 판단
def is_possible(distance):
    cnt = 1 # 지금까지 놓은 물건의 개수
    idx = 0 # dots[idx]에 해당하는 위치에 조건을 만족하면서 물건을 놓을 수 있는지
    for i in range(1, n):
        # dots[idx]에 놓을 수 있다면
        if dots[i] - dots[idx] >= distance:
            # idx 갱신
            idx = i
            cnt+=1
            # m개를 놓았으면 true 반환
            if cnt == m:
                return True
    return False

# 이진 탐색
left, right = 1, 10**9
res = 0 # 결과
while (left <= right):
    mid = (left+right)//2
    # 해당 거리를 만족하면 더 줄임
    if (is_possible(mid)):
        res = max(res, mid)
        left = mid+1
    # 만족하지 않으면 
    else:
        right = mid-1
print(res)
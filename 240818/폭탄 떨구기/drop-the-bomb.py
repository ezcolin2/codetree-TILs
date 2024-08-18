import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# 좌표 오름차순 정렬
arr.sort()

# arr[startIdx]에서 2*r만큼 갔을 때 다음 인덱스
def get_next_idx(startIdx, r):
    nextIdx = startIdx + 1
    while nextIdx < len(arr) and arr[nextIdx] - arr[startIdx] <= 2*r:
        nextIdx += 1
    return nextIdx
        
        
# k개의 폭탄으로 모든 점을 제거할 수 있는지
def is_possible(r):
    startIdx = 0
    cnt = 0
    while startIdx < len(arr):
        startIdx = get_next_idx(startIdx, r)
        cnt += 1
    return cnt <= k

def parametric_search():
    res = sys.maxsize
    left, right = 0, 1000000000
    while left <= right:
        mid = (left+right)//2
        if is_possible(mid):
            right = mid - 1
            res = min(res, mid)
        else:
            left = mid + 1
    return res

print(parametric_search())
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
targets = [int(input()) for _ in range(m)]
# 이진 탐색
def binary_search(target):
    start, end = 0, n-1
    # start가 end보다 커질 때까지 반복
    while (start<=end):
        mid = (start+end)//2
        # 찾으면 인덱스 + 1 반환
        if arr[mid] == target:
            return mid+1
        elif arr[mid] < target:
            start = mid+1
        else:
            end = mid-1
    # 못 찾았다면 -1 반환
    return -1

for i in targets:
    print(binary_search(i))
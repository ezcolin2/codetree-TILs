import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

# num보다 작은 수가 k개 이상 있는지 확인하는 함수
def is_possible(num):
    cnt = 0 # num보다 작은 수의 개수
    # n번 반복
    for i in range(1, n+1):
        cnt += min(n, num//i)
    return cnt >= k

res = sys.maxsize
left, right = 1, n**2
while (left <= right):
    mid = (left + right)//2
    # 가능하다면 결과 갱신하고 수를 낮춰서 판단 
    if is_possible(mid):
        res = min(res, mid)
        right = mid-1
    else:
        left = mid+1

print(res)
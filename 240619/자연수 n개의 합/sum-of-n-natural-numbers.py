import sys
input = sys.stdin.readline

s = int(input())

res = 0

left, right = 1, s
while left <= right:
    mid = (left+right)//2
    if (mid *(mid+1))//2 <= s:
        res = max(res, mid)
        left = mid+1
    else:
        right = mid-1
print(res)
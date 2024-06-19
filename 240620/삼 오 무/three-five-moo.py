import sys
input = sys.stdin.readline
n = int(input())

# 숫자가 몇 번째로 적힌 숫자인지
def order_of_number(num):
    return num- num//3 - num//5 + num//15

# parametric search
left, right = 0, n*10
while (left<=right):
    mid = (left+right)//2
    order = order_of_number(mid)
    # 찾았다면 
    if order == n:
        print(mid)
        exit()
    elif order < n:
        left = mid+1
    else:
        right = mid-1
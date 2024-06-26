import sys
input = sys.stdin.readline
n = int(input())

# 숫자가 몇 번째로 적힌 숫자인지
def order_of_number(num):
    return num- num//3 - num//5 + num//15

# parametric search
left, right = 1, n*10
while (left<=right):
    mid = (left+right)//2
    order = order_of_number(mid)
    # 찾았다면 
    if order == n:
        if (mid %3!=0 and mid%5!=0):
            print(mid)
            exit()
        right -= 1
        continue
    elif order < n:
        left = mid+1
    else:
        right = mid-1
import sys
from collections import defaultdict
input = sys.stdin.readline
import math

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 배열의 모든 값의 개수를 센다.
dic = defaultdict(int)
for i in range(n):
    for j in range(n):
        dic[arr[i][j]] += 1

# 모든 키 값을 가져온다.
keys = list(dic.keys())
keys.sort()

def is_possible(d):    
    # 색칠가능한 개수의 최대값을 구한다.
    max_cnt = 0
    standard = keys[0]
    cnt = dic[standard]
    for i in range(1, len(keys)):
        # 차이가 n 이하라면 이동
        if keys[i] - standard <= d:
            standard = keys[i]
            cnt += dic[standard]
            max_cnt = max(max_cnt, cnt)
        else:
            # 차이가 n 초과라면 max_cnt 갱신하고 cnt 초기화하고 기준 변경
            
            standard = keys[i]
            cnt = dic[standard]
            max_cnt = max(max_cnt, cnt)
    if max_cnt >=32:
        print(d)
    return max_cnt >= math.ceil((n**2)/2)

min_res = sys.maxsize
# 이진 탐색 시작 
left, right = 0, 1000000
while(left <= right):
    mid = (left + right)//2
    if is_possible(mid):
        min_res = min(min_res, mid)
        
        right = mid-1
    else:
        left = mid+1
print(min_res)
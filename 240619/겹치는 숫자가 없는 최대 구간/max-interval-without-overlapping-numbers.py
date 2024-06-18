import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 카운트 배열
count_arr = [0 for _ in range(100000)]

# 최대 구간의 크기
max_val = 0
j = 0
for i in range(n):
    while j < n:
        # 중복이라면 
        if count_arr[arr[j]]+1 >= 2:
            break
            
        # 개수 증가
        count_arr[arr[j]] += 1
        j+=1
    # 최대 구간 크기 갱신
    if j>=n-1:
        j-=1
    max_val = max(max_val, j-i+1)
    
    count_arr[arr[i]] -= 1
print(max_val)
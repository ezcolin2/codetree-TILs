import sys
from collections import defaultdict
input = sys.stdin.readline

input_string, k = input().split()
k = int(k)
left, right = 0, 0
diff_cnt = 0 # 서로 다른 문자의 수

# 문자 별 나온 횟수
cnt = defaultdict(int)
cnt[input_string[0]] += 1
diff_cnt += 1
res = 1
# 길이를 넘을 때까지
while (right < len(input_string)-1):
    # k가 넘지 않으면 
    if (diff_cnt <= k):
        right += 1
        cnt[input_string[right]] += 1
        if (cnt[input_string[right]]==1):
            diff_cnt += 1
        if (diff_cnt <= k):
            res = max(res, right-left+1)
    else:
        cnt[input_string[left]] -= 1
        
        if (cnt[input_string[left]]==0):
            diff_cnt -= 1
        left += 1
print(res)
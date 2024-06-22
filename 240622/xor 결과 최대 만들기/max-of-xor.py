import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
if (m==1):
    print(max(arr))
    exit()
max_val = 0
# 뽑은 숫자들을 모두 xor 연산하는 함수
def xor_combination(combination):
    value = combination[0]
    for i in range(1, len(combination)):
        value = value ^ combination[i]
    return value
# 현재 arr에서 뽑은 숫자들
combination = []
def make_combination(curr_idx, cnt):
    global max_val
    # 모두 탐색했으면 끝
    if (curr_idx == n):
        # 모두 탐색했을 때 m개만큼 뽑았다면
        if cnt == m:
            max_val = max(max_val, xor_combination(combination))
        return
    combination.append(arr[curr_idx])
    make_combination(curr_idx+1, cnt+1)
    combination.pop()

    make_combination(curr_idx+1, cnt)

make_combination(0, 0)
print(max_val)
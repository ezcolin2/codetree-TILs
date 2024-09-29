import sys
input = sys.stdin.readline
n, m = map(int, input().split())
operations = [tuple(map(int, input().split())) for _ in range(m)]
# max_uf[i] : i가 속한 그룹 중 가장 큰 값
max_uf = [i for i in range(100001)]
min_uf = [i for i in range(100001)]
def find_max_root(x):
    if max_uf[x] == x:
        return x
    max_uf[x] = find_max_root(max_uf[x])
    return max_uf[x]
def find_min_root(x):
    if min_uf[x] == x:
        return x
    min_uf[x] = find_min_root(min_uf[x])
    return min_uf[x]

remain_cnt = n
# 남아있는 칸의 개수 반환
def get_remain_boundary_cnt(start, end):
    global remain_cnt
    new_start = find_max_root(start)
    new_end = find_min_root(end)
    different_cnt = 0
    if start != new_start:
        different_cnt += 1
    if end != new_end:
        different_cnt += 1
    for i in range(start, end+1):
        min_uf[i] = start
        max_uf[i] = end
    remain_cnt -= end - start - different_cnt
    return remain_cnt

for a, b in operations:
    print(get_remain_boundary_cnt(a, b))
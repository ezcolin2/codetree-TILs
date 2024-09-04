import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int ,input().split())) for _ in range(m)]
a, b, k = map(int, input().split())

uf = [i for i in range(n+1)]
# sz의 첫 번째 요소는 쓰이지 않고 어차피 정렬하면 마지막이라 안 씀
sz = [[i, 1] for i in range(n+1)]
def find_root(x):
    if x == uf[x]:
        return x
    uf[x] = find_root(uf[x])
    return uf[x]

for x, y in arr:
    root_x = find_root(x)
    root_y = find_root(y)
    
    # 이미 같은 그룹이면 패스
    if root_x == root_y:
        continue
    
    # 다른 그룹이면 넣음
    uf[root_x] = root_y
    sz[root_y][1] += sz[root_x][1]

root_a = find_root(a)
# a 그룹 내부 정점 개수
a_cnt = sz[root_a][1]
# 그룹 수 내림차순 정렬
sz.sort(key = lambda x:(-x[1], -x[0]))
# 그룹 수가 많은 것부터 합친다.
for idx, cnt in sz[:k]:
    # a와 연결할 그룹을 찾는다. 
    root_a = find_root(a)
    root_b = find_root(b)
    # 만약 a와 이미 같은 그룹이라면 패스
    temp_root = find_root(idx)
    if root_a == temp_root:
        continue
    # 만약 b와 같은 그룹이라면 패스
    if root_b == temp_root:
        continue
    uf[temp_root] = root_a
    a_cnt += cnt
print(a_cnt)
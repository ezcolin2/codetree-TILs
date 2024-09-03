import sys
input = sys.stdin.readline
n, m = map(int, input().split())
kind_of_dots = [0] + list(input().rstrip().split())
uf = [i for i in range(n+1)]
def find_root(x):
    if x == uf[x]:
        return x
    uf[x] = find_root(uf[x])
    return uf[x]
arr = [list(map(int, input().split())) for _ in range(m)]
arr.sort(lambda x:x[2])
visited = [False]*(n+1)
res = 0
for a, b, dist in arr:
    # 서로 같은 종류라면 스킵
    if kind_of_dots[a] == kind_of_dots[b]:
        continue
    a_root = find_root(a)
    b_root = find_root(b)
    # 사이클이 생기면 스킵
    if a_root == b_root:
        continue
    visited[a] = True
    visited[b] = True
    uf[a_root] = b_root
    res += dist
for i in visited[1:]:
    if not i:
        print(-1)
        exit()
print(res)
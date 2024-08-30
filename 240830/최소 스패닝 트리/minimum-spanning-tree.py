import sys
input = sys.stdin.readline
n, m = map(int, input().split())
uf = [i for i in range(n+1)]
def find_root(x):
    if x == uf[x]:
        return x
    uf[x] = find_root(uf[x])
    return uf[x]
arr = [list(map(int, input().split())) for _ in range(m)]
arr.sort(key = lambda x:x[2])
res = 0
for a, b, w in arr:
    root_a = find_root(a)
    root_b = find_root(b)
    # 서로 다르다면
    if root_a != root_b:
        uf[root_a] = root_b
        res += w
print(res)